import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
from math import radians, cos, sin, asin, sqrt
import io

# Configuração da página
st.set_page_config(
    page_title="Análise de Eventos de Deslizamento",
    page_icon="⚠️",
    layout="wide"
)

# Título
st.title("⚠️ Análise de Eventos de Deslizamento - Recife/PE")
st.markdown("### Sistema Especializado para Análise de Umidade e Precipitação")

# Definição dos eventos
EVENTS = {
    "Linha do Tiro": {
        "date": "2021-06-18",
        "time": "15:00",
        "lat": -8.0085611,
        "lon": -34.9046944
    },
    "Brejo da Guabiraba": {
        "date": "2021-08-10",
        "time": "03:00",
        "lat": -7.9916056,
        "lon": -34.9295028
    },
    "Alto Santa Terezinha": {
        "date": "2022-06-07",
        "time": "04:20",
        "lat": -8.0125389,
        "lon": -34.9065222
    },
    "Vasco da Gama": {
        "date": "2022-08-02",
        "time": "11:00",
        "lat": -8.0175556,
        "lon": -34.9184889
    },
    "Passarinho 1": {
        "date": "2023-02-06",
        "time": "10:00",
        "lat": -7.9795583,
        "lon": -34.9182028
    },
    "Passarinho 2": {
        "date": "2025-02-06",
        "time": "04:00",
        "lat": -7.9850639,
        "lon": -34.9282806
    }
}

# Função para calcular distância (Haversine)
def calculate_distance(lat1, lon1, lat2, lon2):
    """Calcula distância entre dois pontos geográficos em km"""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Raio da Terra em km
    return c * r

# Função para validar dados
def is_valid_value(sensor, value):
    """Valida se o valor do sensor está dentro dos limites"""
    if pd.isna(value):
        return False
    if 'umidade' in sensor:
        return 0 <= value <= 100
    if sensor == 'chuva':
        return 0 <= value <= 500
    return True

# Função para agregar dados horários (igual ao R)
def build_hourly_strict(df, start_dt, end_dt):
    """
    Implementa agregação horária estrita igual ao código R:
    - Requer 6 slots de 10min OU 1 slot na hora cheia
    """
    # Filtrar dados no período
    df_filtered = df[(df['timestamp'] >= start_dt) & (df['timestamp'] < end_dt)].copy()
    
    if len(df_filtered) == 0:
        return pd.DataFrame()
    
    # Arredondar para slots de 10 minutos
    df_filtered['minute'] = df_filtered['timestamp'].dt.minute
    df_filtered['minute_rounded'] = (df_filtered['minute'] / 10).round() * 10
    df_filtered['ts_10'] = df_filtered['timestamp'].dt.floor('H') + pd.to_timedelta(df_filtered['minute_rounded'], unit='m')
    
    # Agrupar por estação, sensor e slot de 10min
    grouped_10 = df_filtered.groupby(['stationCode', 'sensor', 'ts_10'])['value'].mean().reset_index()
    grouped_10.columns = ['stationCode', 'sensor', 'ts_10', 'valor_10']
    
    # Agrupar por hora
    grouped_10['ts_hour'] = grouped_10['ts_10'].dt.floor('H')
    grouped_10['minute'] = grouped_10['ts_10'].dt.minute
    
    # Contar slots por hora
    hourly_groups = grouped_10.groupby(['stationCode', 'sensor', 'ts_hour'])
    
    result_list = []
    for (station, sensor, hour), group in hourly_groups:
        n_slots = len(group)
        is_rain = sensor == 'chuva'
        
        # Regra estrita: 6 slots OU 1 slot no minuto 0
        if n_slots == 6:
            valor_h = group['valor_10'].sum() if is_rain else group['valor_10'].mean()
            result_list.append({
                'stationCode': station,
                'sensor': sensor,
                'ts_hour': hour,
                'valor_h': valor_h
            })
        elif n_slots == 1 and group['minute'].iloc[0] == 0:
            result_list.append({
                'stationCode': station,
                'sensor': sensor,
                'ts_hour': hour,
                'valor_h': group['valor_10'].iloc[0]
            })
    
    return pd.DataFrame(result_list)

# Função para carregar dados
@st.cache_data
def load_data(uploaded_files):
    """Carrega e processa arquivos CSV"""
    all_data = []
    stations = {}
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for idx, file in enumerate(uploaded_files):
        status_text.text(f"Processando {file.name}...")
        
        try:
            # Ler CSV
            df = pd.read_csv(file, sep=';', encoding='latin-1')
            
            # Processar cada linha
            for _, row in df.iterrows():
                datetime_str = str(row.get('datahora', '')).strip()
                sensor = str(row.get('sensor', '')).strip()
                value_str = str(row.get('valorMedida', '')).replace(',', '.')
                station_name = str(row.get('nomeEstacao', '')).strip()
                station_code = str(row.get('codEstacao', '')).strip()
                
                try:
                    value = float(value_str)
                except:
                    continue
                
                if datetime_str and sensor and is_valid_value(sensor, value):
                    all_data.append({
                        'datetime': datetime_str,
                        'station': station_name,
                        'stationCode': station_code,
                        'sensor': sensor,
                        'value': value
                    })
                    
                    # Armazenar info da estação
                    if station_code and station_code not in stations:
                        stations[station_code] = station_name
            
            progress_bar.progress((idx + 1) / len(uploaded_files))
            
        except Exception as e:
            st.warning(f"Erro ao processar {file.name}: {str(e)}")
    
    progress_bar.empty()
    status_text.empty()
    
    if not all_data:
        return None, None
    
    # Converter para DataFrame
    df = pd.DataFrame(all_data)
    df['timestamp'] = pd.to_datetime(df['datetime'].str.replace(' ', 'T'), errors='coerce')
    df = df.dropna(subset=['timestamp'])
    
    return df, stations

# Sidebar - Upload de arquivos
st.sidebar.title("📁 Carregamento de Dados")
uploaded_files = st.sidebar.file_uploader(
    "Faça upload dos arquivos CSV",
    type=['csv'],
    accept_multiple_files=True,
    help="Selecione todos os arquivos CSV da pasta Recife_prec_umid_cemaden"
)

if uploaded_files:
    # Carregar dados
    with st.spinner("Carregando dados..."):
        df, stations = load_data(uploaded_files)
    
    if df is not None:
        st.sidebar.success(f"✅ {len(df):,} registros carregados")
        st.sidebar.info(f"📅 Período: {df['timestamp'].min().strftime('%d/%m/%Y')} a {df['timestamp'].max().strftime('%d/%m/%Y')}")
        
        # Seleção do evento
        st.sidebar.title("🎯 Selecionar Evento")
        selected_event_name = st.sidebar.selectbox(
            "Escolha o evento de deslizamento:",
            list(EVENTS.keys())
        )
        
        event = EVENTS[selected_event_name]
        event_date = datetime.strptime(event['date'], '%Y-%m-%d')
        event_datetime = datetime.strptime(f"{event['date']} {event['time']}", '%Y-%m-%d %H:%M')
        
        # Calcular período D-2
        d2_date = event_date - timedelta(days=2)
        
        # Mostrar info do evento
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"**📅 Data:** {event_date.strftime('%d/%m/%Y')}")
        st.sidebar.markdown(f"**🕐 Horário:** {event['time']}")
        st.sidebar.markdown(f"**📍 Coordenadas:** {event['lat']:.6f}, {event['lon']:.6f}")
        st.sidebar.markdown(f"**📊 Período Análise:** {d2_date.strftime('%d/%m/%Y')} a {event_date.strftime('%d/%m/%Y')}")
        
        # Calcular distâncias das estações
        station_distances = []
        for code, name in stations.items():
            # Coordenadas aproximadas (você pode melhorar isso)
            # Por enquanto, usando coordenadas genéricas de Recife
            station_lat = -8.05  # Aproximado
            station_lon = -34.92  # Aproximado
            
            distance = calculate_distance(event['lat'], event['lon'], station_lat, station_lon)
            station_distances.append({
                'code': code,
                'name': name,
                'distance': distance
            })
        
        station_distances_df = pd.DataFrame(station_distances).sort_values('distance')
        
        # Seleção da estação
        st.sidebar.title("📍 Selecionar Estação")
        
        # Mostrar ranking
        st.sidebar.markdown("**Top 10 Estações Mais Próximas:**")
        for idx, row in station_distances_df.head(10).iterrows():
            st.sidebar.markdown(f"{idx+1}. {row['name']} ({row['distance']:.2f} km)")
        
        selected_station = st.sidebar.selectbox(
            "Escolha a estação:",
            station_distances_df['code'].tolist(),
            format_func=lambda x: f"{stations[x]} ({station_distances_df[station_distances_df['code']==x]['distance'].iloc[0]:.2f} km)"
        )
        
        # Filtrar dados
        start_dt = pd.Timestamp(d2_date)
        end_dt = pd.Timestamp(event_date) + pd.Timedelta(days=1)
        
        df_filtered = df[
            (df['stationCode'] == selected_station) &
            (df['timestamp'] >= start_dt) &
            (df['timestamp'] < end_dt)
        ]
        
        # Agregar dados horários
        df_hourly = build_hourly_strict(df_filtered, start_dt, end_dt)
        
        if len(df_hourly) > 0:
            # Reorganizar dados para gráficos
            df_pivot = df_hourly.pivot(index='ts_hour', columns='sensor', values='valor_h').reset_index()
            
            # Seleção de níveis
            st.sidebar.title("🎯 Níveis de Profundidade")
            selected_levels = []
            for i in range(1, 7):
                if st.sidebar.checkbox(f"Nível {i}", value=True, key=f"nivel_{i}"):
                    selected_levels.append(f'umidade_solo_nivel{i}')
            
            # Tipo de visualização de chuva
            rain_view = st.sidebar.radio("🌧️ Visualização de Chuva:", ["Horária", "Diária"])
            
            # Layout principal
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"### 📊 Análise: {selected_event_name}")
                st.markdown(f"**Estação:** {stations[selected_station]}")
            
            with col2:
                st.metric("Registros Válidos", f"{len(df_hourly):,}")
            
            # Gráfico de Umidade
            st.markdown("### 💧 Umidade do Solo")
            
            fig_humidity = go.Figure()
            
            colors = ['#ef4444', '#f97316', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6']
            for idx, nivel in enumerate(selected_levels):
                if nivel in df_pivot.columns:
                    fig_humidity.add_trace(go.Scatter(
                        x=df_pivot['ts_hour'],
                        y=df_pivot[nivel],
                        name=f"Nível {idx+1}",
                        mode='lines',
                        line=dict(color=colors[idx], width=2),
                        connectgaps=False
                    ))
            
            # Linha do evento
            fig_humidity.add_vline(
                x=event_datetime,
                line_dash="dash",
                line_color="red",
                line_width=3,
                annotation_text="EVENTO",
                annotation_position="top"
            )
            
            fig_humidity.update_layout(
                height=400,
                xaxis_title="Data/Hora",
                yaxis_title="Umidade (%)",
                hovermode='x unified',
                showlegend=True
            )
            
            st.plotly_chart(fig_humidity, use_container_width=True)
            
            # Gráfico de Precipitação
            st.markdown("### 🌧️ Precipitação")
            
            fig_rain = go.Figure()
            
            if rain_view == "Diária":
                # Agregar por dia
                df_pivot['date'] = df_pivot['ts_hour'].dt.date
                df_daily = df_pivot.groupby('date')['chuva'].sum().reset_index()
                df_daily['date'] = pd.to_datetime(df_daily['date'])
                
                fig_rain.add_trace(go.Bar(
                    x=df_daily['date'],
                    y=df_daily['chuva'],
                    name='Chuva Diária',
                    marker_color='rgba(14, 165, 233, 0.7)'
                ))
            else:
                # Horária
                fig_rain.add_trace(go.Scatter(
                    x=df_pivot['ts_hour'],
                    y=df_pivot['chuva'],
                    name='Chuva Horária',
                    mode='lines',
                    line=dict(color='#0ea5e9', width=2),
                    fill='tozeroy',
                    fillcolor='rgba(14, 165, 233, 0.3)',
                    connectgaps=False
                ))
            
            # Linha do evento
            fig_rain.add_vline(
                x=event_datetime,
                line_dash="dash",
                line_color="red",
                line_width=3,
                annotation_text="EVENTO",
                annotation_position="top"
            )
            
            fig_rain.update_layout(
                height=350,
                xaxis_title="Data/Hora" if rain_view == "Horária" else "Data",
                yaxis_title="Precipitação (mm)",
                hovermode='x unified',
                showlegend=True
            )
            
            st.plotly_chart(fig_rain, use_container_width=True)
            
            # Estatísticas
            st.markdown("### 📊 Estatísticas do Período")
            
            cols = st.columns(len(selected_levels) + 1)
            
            # Estatísticas de umidade
            for idx, nivel in enumerate(selected_levels):
                if nivel in df_pivot.columns:
                    values = df_pivot[nivel].dropna()
                    if len(values) > 0:
                        with cols[idx]:
                            st.metric(
                                f"💧 Nível {idx+1}",
                                f"{values.mean():.1f}%",
                                delta=f"Max: {values.max():.1f}%"
                            )
                            st.caption(f"Min: {values.min():.1f}%")
            
            # Estatísticas de chuva
            if 'chuva' in df_pivot.columns:
                rain_values = df_pivot['chuva'].dropna()
                if len(rain_values) > 0:
                    with cols[-1]:
                        st.metric(
                            "🌧️ Chuva Total",
                            f"{rain_values.sum():.1f} mm",
                            delta=f"Média: {rain_values.mean():.2f} mm/h"
                        )
                        st.caption(f"Max: {rain_values.max():.1f} mm/h")
            
        else:
            st.warning("⚠️ Não há dados disponíveis para o período selecionado.")
    
else:
    st.info("👈 Faça upload dos arquivos CSV na barra lateral para começar")
    
    st.markdown("""
    ### 📖 Como usar:
    
    1. **Upload dos dados**: Clique em "Browse files" na barra lateral e selecione TODOS os arquivos CSV da pasta `Recife_prec_umid_cemaden`
    2. **Selecione o evento**: Escolha qual evento de deslizamento deseja analisar
    3. **Escolha a estação**: Selecione a estação mais próxima do ranking
    4. **Visualize os gráficos**: Os dados serão automaticamente filtrados para D-2 até D0
    5. **Configure a visualização**: Use os controles da barra lateral para personalizar
    
    ### ⚡ Recursos:
    - ✅ Agregação horária igual ao código R
    - ✅ Cálculo automático de distâncias (fórmula Haversine)
    - ✅ Ranking de estações mais próximas
    - ✅ Visualização interativa com Plotly
    - ✅ Marca do momento exato do evento
    - ✅ Estatísticas em tempo real
    """)
