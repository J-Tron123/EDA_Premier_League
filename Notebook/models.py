import pandas as pd, numpy as np, warnings, requests, plotly.express as px
from bs4 import BeautifulSoup as bs

warnings.filterwarnings("ignore")

# Instancio las funciones y las separo en clases 

class Scrapers():
    def __init__():
        pass

    def transferscrap(year):
        """
        Esta función scrapea los nombres de los equipos y sus valores de plantilla de una temporada específica de la Premier League 
        que se le pasa como parametro ```year```
        """
        web = f"https://www.transfermarkt.es/premier-league/startseite/wettbewerb/GB1/plus/?saison_id={year}" # Web atacada
        headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
        total = []
        season = []

        response = requests.get(web, headers=headers)
        soup = bs(response.content, "lxml")
        team = soup.find_all("tr", class_="odd")

        for i in team:
            if i.text[-1] == "€":                              # Separo los valores de las plantillas del resto de información 
                season.append(i.text + str(year) + "-" + str(year+1)) # y lo concateno con la temporada

        team = soup.find_all("tr", class_="even")

        for i in team:
            if i.text[-1] == "€":    
                season.append(i.text + str(year) + "-" + str(year+1))

        team = soup.find_all("tr", class_="odd selected")

        for i in team:
            if i.text[-1] == "€":    
                season.append(i.text + str(year) + "-" + str(year+1))

        total.append(season)

        team = []
        value = []
        season = []
        for i in total:
            for j in i:
                k = j.split()[:2] 
                if k == "Brighton &":
                    k = j.split()[:4]
                elif "Queens" in k or "Ham" in k or "Bromwich" in k: # Separo por equipos para agrupar cada equipo con su
                    k = j.split()[:3]                                # información
                l = j.split()[-3:-1]
                if l == ["mil", "mill."]:
                    l = j.split()[-4:-1]
                m = j.split()[-1]
                team.append(k)
                value.append(l)
                season.append(m)

        data = {"Season" : season, "Team" : team, "Value mill €" : value}   # Los añado a un diccionario para convertirlo 
                                                                            # luego en un DataFrame
        values = pd.DataFrame(data)
        values["Season"] = values.apply(Limpiadoras().clean_row, args = ("Season",), axis=1) # Creo las columnas que quiero
        values["Team"] = values.apply(Limpiadoras().join_row, args = ("Team",), axis=1)      # y retrno un DataFrame
        values["Value mill €"] = values.apply(Limpiadoras().join_row, args = ("Value mill €",), axis=1)
        values["Value mill €"] = values.apply(Limpiadoras().float_value, args = ("Values mill €",), axis=1)

        return values

    def transferscrap_money(year):
        """
        Esta función scrapea los nombres de los equipos y sus gastos y beneficios en fichajes de una temporada específica de la Premier League 
        que se le pasa como parametro ```year```
        """
        web = "https://www.transfermarkt.es" # Web atacada
        first = f"/premier-league/startseite/wettbewerb/GB1/plus/?saison_id={year}"
        headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
        response = requests.get(web + first, headers=headers)
        soup = bs(response.content, "lxml")

        teams = soup.find_all("td", class_="hauptlink no-border-links") # Encuentro los datos que quiero por las etiquetas 
        links = soup.find_all("td", class_="no-border-links hauptlink") # en las que están señalados en la web

        data_1 = {"Team" : []}
        data_2 = {"Season" : [],"Team" : [], "profits" : [], "losses" : []} # Los agrupo en un diccionario de listas para luego
                                                                            # convertir eso en un DataFrame
        for i in links:
            data_1["Team"].append(i.find("a")["title"])

        df_data_1 = pd.DataFrame(data_1)

        for i in teams:
            response = requests.get(web + i.find("a")["href"], headers=headers)
            soup = bs(response.content, "lxml")
            data_2["Team"].append(" ".join(soup.find("div", class_="dataName").text.split())) # En este bucle repito el proceso anterior
            data_2["profits"].append(soup.find(class_="greentext rechts").text.split()[0])    # pero para conseguir el equipo y su posición
            data_2["losses"].append(soup.find(class_="redtext rechts").text.split()[0])       # en la calsificación
            data_2["Season"].append(str(year) + "-" + str(year+1))

        df_data_2 = pd.DataFrame(data_2)

        df = df_data_1.merge(df_data_2)
        df["profits"] = df.apply(Limpiadoras().float_money(args = ("profits",)), axis=1)# Limpio comas de euros de los datos extraídos
        df["losses"] = df.apply(Limpiadoras().float_money(args = ("losses",)), axis=1)  # y multiplico por mil para los que son de mil millones
                                                                                        # ya que vienen como número natural
        return df                                                                       # Retorno un DataFrame

class Limpiadoras():
    def __init__():
        pass

    def clean_row(row, column_name):
        """
        Esta función es para limpiar datos obtenidos de la función transferscrap
        """
        for i in row[column_name]:
            if i == "-":
                continue
            elif i == ",":
                row[column_name] = row[column_name].replace(i, ".")
            else:
                try:
                    float(i)
                except:
                    row[column_name] = row[column_name].replace(i, "")
        return row[column_name]

    def join_row(row, column_name):
        """
        Esta función es para limpiar datos obtenidos de la función transferscrap
        """
        row[column_name] = " ".join(row[column_name])
        return row[column_name]

    def float_value(row, column_name):
        """
        Esta función es para limpiar datos obtenidos de la función transferscrap
        """
        row = row[column_name].replace("€", "").replace("mill.", "").replace(",", ".")
        if "mil" in row:
            row = "".join(row.replace("mil", ""))
            row = float(row)*1000
        row = float(row)
        return row

    def float_money(row, column_name):
        """
        Esta función es para limpiar datos obtenidos de la función transferscrap_money
        """
        if "." in row[column_name]:
            return float(row[column_name])
        elif "," in row[column_name]:
            return float(row[column_name].replace(",", "."))
        else:
            lon = len(str(row[column_name]))
            return float(row[column_name]) / (10**lon)

class Competicion():
    def __init__():
        pass

    def promedio_temporadas(df=pd.DataFrame, competicion=str, lista=[]):
        '''
        Esta función la utilizo para separar el dataframe total_standings por posiciones en la tabla de clasificación
        '''
        if len(lista) == 1:
            resultado = df[(df["Pos"] == lista[0])].reset_index().drop("index", axis=1)
            media_resultado = pd.DataFrame(dict(zip(resultado.mean().index, np.round(resultado.mean().values))), index=[1])
            media_resultado["Season"] = "Promedio de las temporadas"
            media_resultado["Team"] = f"{competicion} promedio"
            return pd.concat([resultado, media_resultado], ignore_index=True, axis=0)

        elif len(lista) == 2:
            resultado = df[(df["Pos"] >= lista[0]) & (df["Pos"] <= lista[1])].reset_index().drop("index", axis=1)
            media_resultado = pd.DataFrame(dict(zip(resultado.mean().index, np.round(resultado.mean().values))), index=[1])
            media_resultado["Pts"] += 1
            media_resultado["Season"] = "Promedio de las temporadas"
            media_resultado["Team"] = f"{competicion} promedio"
            return pd.concat([resultado, media_resultado], ignore_index=True, axis=0)

        else:
            return "lista debe tener solo 2 elementos"

    def data_coste(elemento, df=pd.DataFrame):
        '''
        Esta función la utilizo para calcular el coste de alguna estadística, por ejemplo, el coste de cada gol a favor
        '''
        coste = np.round(df.groupby(["Team"])[["balance", "Pos", elemento]].mean()).reset_index()
        coste[f"mill/{elemento}"] = np.round(coste["balance"] / coste[elemento], 3)
        media_coste = pd.DataFrame(dict(zip(coste.mean().index, np.round(coste.mean().values, 4))), index=[1])
        media_coste["Team"] = f"Promedio de coste de {elemento}"
        coste = pd.concat([coste, media_coste], ignore_index=True, axis=0)
        return coste

class Graficas():
    def __init__():
        pass

    def hist_(titulo, df, x, histfunc="count", orient="v", y=None, columnas=None):
        '''
        Esta función la utilizo para generar un histograma de la librería plotly
        '''
        color = x
        if orient != "v":
            color = y
        if isinstance(color, list):
            if not y:
                fig = px.histogram(df, x=x[0], nbins=10, color=color, histfunc=histfunc, barmode="stack", marginal="rug", hover_data=columnas)
            else:
                histfunc = "avg"
                fig = px.histogram(df, x=x, y=y, color=color[0], histfunc=histfunc, barmode="group", marginal="rug", hover_data=columnas)
        else:
            if not y:
                fig = px.histogram(df, x=x, nbins=10, color=color, histfunc=histfunc, barmode="stack", marginal="rug", hover_data=columnas)
            else:
                histfunc = "avg"
                fig = px.histogram(df, x=x, y=y, color=color, histfunc=histfunc, barmode="stack", marginal="rug", hover_data=columnas)
        fig.update_layout(bargap=0.2, title=titulo)
        fig.show()

    def box_(titulo, df, x, y, se_pinta=None, no_se_pinta=None):
        '''
        Esta función la utilizo para generar un boxplot de la librería plotly
        '''
        if not isinstance(x, list):
            fig = px.box(data_frame=df, x=x, y=y, points="all", color=x, hover_data=df.columns)
            fig.update_layout(bargap=0.2, title=titulo)
            fig.show()
        else:
            fig = px.box(data_frame=df, x=x[no_se_pinta], y=y, points="all", color=x[se_pinta], hover_data=df.columns)
            fig.update_layout(bargap=0.2, title=titulo)
            fig.show()

    def scatter_(titulo, df, x, y=None, se_pinta=None, orient="v"):
        '''
        Esta función la utilizo para generar un scatter plot de la librería plotly
        '''
        color = x
        if orient == "h":
            color = y
        if isinstance(color, list):
            if not y:
                fig = px.scatter(data_frame=df, x=x, color=color[se_pinta], symbol=color[se_pinta], hover_data=df.columns)
            else:
                fig = px.scatter(data_frame=df, x=x, y=y, color=color[se_pinta], symbol=color[se_pinta], hover_data=df.columns)
        else:
            if not y:
                fig = px.scatter(data_frame=df, x=x, color=color, symbol=color, hover_data=df.columns)
            else:
                fig = px.scatter(data_frame=df, x=x, y=y, color=color, symbol=color, hover_data=df.columns)
        fig.update_traces(marker_size=10)
        fig.update_layout(title=titulo)
        fig.show()

    def heat_(titulo, df, x, y):
        '''
        Esta función la utilizo para generar un mapa de calor de la librería plotly
        '''
        df = df[[x, y]]
        correlation = df.corr()
        transposed_corr = correlation[::-1]
        fig = px.imshow(transposed_corr)
        fig.update_layout(title=titulo)
        fig.show()
