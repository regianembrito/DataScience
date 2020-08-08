## Documentação do rtweet https://cran.r-project.org/web/packages/rtweet/rtweet.pdf

library(rtweet)

setwd('C:\\DataScience\\BootCamp\\ColetaTwitter') # Define diretório de trabalho

# Autenticação
token <- create_token(app = "Coletor IGTI - Rbrito", consumer_key='PmIJILL1Doghf1IIbve6ZbH6B',
                      consumer_secret = 'XMLNS1B9CkRTXggBZSvNR6AnXPiZedhECISE4KMOyUgBfTS9gU',
                      access_token = '115965475-1YzmIChewhoW0tdmB4qrzFqNYFRd0pD5Gi6XPvqO',
                      access_secret = 'bCYkdNdbBYP0a87ezYwtPgE5Up7zfMbHzmpNiPGSk9aqg')

# Parâmetros de busca
screen_name <- "jairbolsonaro"

# Buscando
tweets <- get_timeline(screen_name, n=1000, include_rts=TRUE, exclude_replies=TRUE)

# Salbando o vetor de tweets como csv e apenas o Texto em txt na codificação de português
write_as_csv(tweets, "TweetsByNameRawData.csv", fileEncoding = "latin1//TRANSLIT")


## Plota a serie temporal dos tweets
ts_plot(tweets, "3 hours") +
  ggplot2::theme_minimal() + 
  ggplot2::theme(plot.title = ggplot2::element_text(face = "bold")) +
  ggplot2::labs (
    x = NULL, y = NULL,
    title = 'Frequencia de tweets da conta "jairbolsonar" nos últimos 9 dias',
    subtitle = 'Contagem de tweets agregados em intervalos de 3 horas',
    caption = '\nFont: Dados coletado do Twitter com o pacote rtweet'
  )