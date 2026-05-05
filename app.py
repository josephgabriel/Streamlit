import streamlit as st

st.sidebar.image('IFCE.jpg', width=100)
st.sidebar.title("Predição")
st.sidebar.markdown("Campus Tiangua")

# Header 01
def carregar_pagina01():
    from paginas.header01.app1 import main
    main()

def carregar_pagina02():
    from paginas.header01.app2 import main
    main()

def carregar_pagina03():
    from paginas.header01.app3 import main
    main()

st.sidebar.header("Visão Geral")
st.sidebar.button('Dashboard', icon=":material/pie_chart:", on_click=carregar_pagina01)
st.sidebar.button('Predição Individual',icon=":material/person:", on_click=carregar_pagina02)
st.sidebar.button('Alunos em Risco', icon=":material/warning:", on_click=carregar_pagina03)

# Header 02
def carregar_pagina04():
    from paginas.header02.app4 import main
    main()

def carregar_pagina05():
    from paginas.header02.app5 import main
    main()

def carregar_pagina06():
    from paginas.header02.app6 import main
    main()

st.sidebar.header("Análise")
st.sidebar.button('Cursos', icon=":material/analytics:", on_click=carregar_pagina04)
st.sidebar.button('Fatores de Risco', icon=":material/group:", on_click=carregar_pagina05)
st.sidebar.button('Tendências', icon=":material/insights:", on_click=carregar_pagina06)

# Header 03
def carregar_pagina07():
    from paginas.header03.app7 import main
    main()

def carregar_pagina08():
    from paginas.header03.app8 import main
    main()

def carregar_pagina09():
    from paginas.header03.app9 import main
    main()

st.sidebar.header("Sistema")
st.sidebar.button('Importar Dados',icon=":material/upload:", on_click=carregar_pagina07)
st.sidebar.button('Relatorios',icon=":material/description:", on_click=carregar_pagina08)
st.sidebar.button('Configurações', icon=":material/settings:", on_click=carregar_pagina09)
