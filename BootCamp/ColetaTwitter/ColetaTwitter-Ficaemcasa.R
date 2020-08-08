#Documentacao do rtweet https:LISta.r-project.org/web/packages/rweet/rtweet. pdf

library(rtweet) #Usa a API do twitter library(maps) plotar mapas

setwd("C:\\DataScience\\BootCamp\\ColetaTwitter") #Define diretório de trabalho

token <- create_token(app = "Coletor IGTI - Rbrito", consumer_key='PmIJILL1Doghf1IIbve6ZbH6B',
                      consumer_secret = 'XMLNS1B9CkRTXggBZSvNR6AnXPiZedhECISE4KMOyUgBfTS9gU',
                      access_token = '115965475-1YzmIChewhoW0tdmB4qrzFqNYFRd0pD5Gi6XPvqO',
                      access_secret = 'bCYkdNdbBYP0a87ezYwtPgE5Up7zfMbHzmpNiPGSk9aqg')

# Parâmetros de busca
search.string <- c("#ficaemcasa OR #coronavirus OR #covid OR #covid-19 OR #covid19") 
type = "mixed" # "recent", "mixed" ou "popular
#include_rt (TRUE ou FALSE) - usado para indicar se inclui retweets ou não na pesquisa
#retryonratimit (TRUE OU FALSE) - usado para indicar se continua ou não depois do limite de 18000 tweets

# Buscando
tweets <- search_tweets (search.string, n=18000, lang="pt", type=type,
                         include_rts = FALSE, retryonratelimit = TRUE)
                      
# Salvando o vetor de tweets como Csv e apenas o Texto em TXT na codificação do portugues
write_as_csv(tweets, "TweetsRawData.csv", fileEncoding = "latin1//TRANSLIT")
write.table(tweets$text, "TweetsRawData.txt", fileEncoding = "latin1//TRANSLIT")

tweets <- lat_lng(tweets) ##cria lat/1gn variaveis usando todos os tweets dosponiveis

# plotar o mapa do Brasil

par(mar=c(0,0,0,0)) # Função par define ou ajusta os parâmetros de plotagem. Parametro mar ajusta as margens. 
map("world", "brazil", lwd = 0.3, fill = T, col = "grey95")

map(,,add=T)

map.axes()

map.scale(ratio=T, cex=0.3)

abline(h=0, lty = 2)

map.cities(country = "Brazil",minpop = 2000000, pch=15, cex=0.9) # pacote maps

# Adicina os tweets ao mapa

with(tweets, points (lng, lat, pch = 20, cex = .75, col = rgb(0, .3, .7, .75)))