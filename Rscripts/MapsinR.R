library("ggplot2")
library("rworldmap")
# Loading all the necessary packages

data <-read.csv(file="ggmap.csv", header=T, sep=',')
# Loading the data into R

data = data[-c(1),]
# Removing the second header line, because only the first is needed

data$long = as.numeric(as.character(data$long))
data$lat = as.numeric(as.character(data$lat))
data$dep = as.numeric(as.character(data$dep))
data$year = as.numeric(as.character(data$year))
# Making sure all the variables are numeric

data$dep = data$dep * -1
# Making the depth values negative, because they are under sealevel

mapWorld <- borders("world", colour="gray50", fill="gray50")
# Creates a world map under the variable 'mapWorld'

allyear<-as.factor(unique(data$"year"))
# Creating a factor with 12 levels, each for one year of data

for ( i in seq_along(allyear)){
# Creating a forloop that for every year in allyear the following ggplot creates:
    panda <- ggplot(data[data$"year"==allyear[i],],aes(long,lat,color=dep)) +
    mapWorld +
    theme_minimal()+ 
    geom_point(cex=2)+
    scale_colour_gradient2(limits=c(min(data$dep),max(data$dep)),
                           low="purple4",mid="turquoise1", high="orchid",
                           name="Depth\nin meters", guide="colourbar") + 
    xlab("Longitude (°East)")+
    ylab("Latitude (°North)")+ 
    theme(plot.background = element_blank(),panel.grid.major = element_blank(),
          panel.grid.minor = element_blank())+
    theme(panel.border = element_blank())+
    theme(legend.position = "right")+
    theme(plot.title = element_text(size=25),axis.title = element_text(size=22),
          axis.text = element_text(size=22),legend.title=element_text(size=16),
          legend.text=element_text(size=14))+
    theme(strip.text.x = element_blank())+
    theme(plot.background=element_rect(fill="white",colour="white"))+
    ggtitle(allyear[i])
  # Saving the ggplots as .png with the year of data as the name
  ggsave(plot=panda,filename=paste(allyear[i],".png",sep=""),width=16,height=8,dpi=100)
}
