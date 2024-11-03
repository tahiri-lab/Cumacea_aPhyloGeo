# Charger les bibliothèques nécessaires
library(ggplot2)
library(dplyr)
library(maps)
library(mapdata)

# Lire le fichier Excel
data_map <- read.csv(file = "SciPy_2024_data_preprocessing.csv", header=T)

# Définir les couleurs pour chaque secteur
sector_colors <- c(
  "Denmark Strait" = "red",
  "Iceland Basin" = "blue",
  "Irminger Basin" = "green",
  "Norwegian Sea" = "purple",
  "Norwegian Basin" = "orange"
)

# Calculer le nombre d'échantillons par point
data_map_count <- data_map %>%
  group_by(Long_start_dec, Lat_end_dec, Sector) %>%
  summarise(N = n(), .groups = 'drop')  # Compter les échantillons

# Créer la carte
world_map <- map_data("world")

# Créer la carte avec une couleur de fond
ggplot() +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "lightgrey") +
  geom_point(data = data_map_count, aes(x = Long_start_dec, y = Lat_end_dec, color = Sector), size = 7) +
  geom_text(data = data_map_count, aes(x = Long_start_dec - 0.5, y = Lat_end_dec, label = N), 
            vjust = 0.5, hjust = 1, size = 5.5, color = "black") +  # Ajouter le texte à gauche des points
  scale_color_manual(values = sector_colors) +
  labs(x = "Longitude (DD) at the start of sampling", y = "Latitude (DD) at the end of sampling", color = "Oceanic sectors") +
  theme_minimal() +
  coord_fixed(1.3) +  # Pour un meilleur aspect de la carte
  xlim(-32.5, -10) +  # Limites de longitude pour zoomer
  ylim(55, 68.1) +    # Limites de latitude pour zoomer
  theme(panel.background = element_rect(fill = "lightblue"),  # Couleur de fond
        panel.grid.major = element_line(color = "transparent"), # Supprimer les lignes de grille majeures
        panel.grid.minor = element_line(color = "transparent"), # Supprimer les lignes de grille mineures
        axis.text.x = element_text(angle = 45, hjust = 1, size = 18),  # Ajuster le texte de l'axe des x
        axis.text.y = element_text(size = 18),   # Ajuster le texte de l'axe des y
        axis.title.x = element_text(size = 25),  # Augmenter la taille du titre de l'axe x
        axis.title.y = element_text(size = 25),  # Augmenter la taille du titre de l'axe y
        plot.title = element_text(hjust = 0.5),  # Centrer le titre
        legend.title = element_text(size = 23),  # Taille du titre de la légende
        legend.text = element_text(size = 19),   # Taille du texte de la légende
        legend.key.size = unit(3.9, "cm"))       # Taille de la clé de la légende




