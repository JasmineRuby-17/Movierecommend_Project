import pandas as pd

movies = [
    # Vijay
    ("Leo (2023)", "Action Thriller"),
    ("Master (2021)", "Action Drama"),
    ("Bigil (2019)", "Sports Drama"),
    ("Sarkar (2018)", "Political Drama"),
    ("Mersal (2017)", "Action Thriller"),
    ("Theri (2016)", "Action Drama"),
    ("Kaththi (2014)", "Action Drama"),
    ("Thuppakki (2012)", "Action Thriller"),
    ("Nanban (2012)", "Comedy Drama"),
    ("Ghilli (2004)", "Action Romance"),
    ("Thirupaachi (2005)", "Action Drama"),
    ("Sivakasi (2005)", "Action Drama"),
    ("Pokkiri (2007)", "Action Crime"),
    ("Velayudham (2011)", "Action Comedy"),

    # Ajith
    ("Viswasam (2019)", "Action Family"),
    ("Valimai (2022)", "Action Thriller"),
    ("Vedalam (2015)", "Action Drama"),
    ("Yennai Arindhaal (2015)", "Crime Thriller"),
    ("Mankatha (2011)", "Crime Thriller"),
    ("Billa (2007)", "Action Crime"),

    # Rajinikanth
    ("Jailer (2023)", "Action Thriller"),
    ("Petta (2019)", "Action Drama"),
    ("Kaala (2018)", "Action Drama"),
    ("Kabali (2016)", "Action Crime"),
    ("Sivaji (2007)", "Action Drama"),
    ("Chandramukhi (2005)", "Horror Comedy"),

    # Kamal Haasan
    ("Vikram (2022)", "Action Thriller"),
    ("Dasavatharam (2008)", "Action Sci-Fi"),
    ("Indian (1996)", "Action Drama"),
    ("Anbe Sivam (2003)", "Drama Comedy"),
    ("Nayakan (1987)", "Crime Drama"),
    ("Hey Ram (2000)", "Historical Drama"),

    # Suriya
    ("Soorarai Pottru (2020)", "Drama"),
    ("Jai Bhim (2021)", "Legal Drama"),
    ("Ayan (2009)", "Action Crime"),
    ("Singam (2010)", "Action Thriller"),
    ("Singam 2 (2013)", "Action Thriller"),
    ("24 (2016)", "Sci-Fi Thriller"),
    ("Ghajini (2005)", "Action Thriller"),

    # Dhanush
    ("Asuran (2019)", "Action Drama"),
    ("Karnan (2021)", "Action Drama"),
    ("VIP (2014)", "Comedy Drama"),
    ("Maari (2015)", "Action Comedy"),
    ("Thiruchitrambalam (2022)", "Romance Comedy"),
    ("Raanjhanaa (2013)", "Romance Drama"),

    # Vijay Sethupathi
    ("96 (2018)", "Romance Drama"),
    ("Pizza (2012)", "Horror Thriller"),
    ("Super Deluxe (2019)", "Crime Drama"),
    ("Naanum Rowdy Dhaan (2015)", "Action Comedy"),

    # Sivakarthikeyan
    ("Doctor (2021)", "Action Comedy"),
    ("Don (2022)", "Comedy Drama"),
    ("Remo (2016)", "Romance Comedy"),

    # Other Tamil Hits
    ("Kaithi (2019)", "Action Thriller"),
    ("Vada Chennai (2018)", "Crime Drama"),
    ("Pariyerum Perumal (2018)", "Drama"),
    ("Aruvi (2017)", "Drama"),
    ("Madras (2014)", "Drama Crime"),
    ("Visaranai (2015)", "Crime Thriller"),
    ("Subramaniapuram (2008)", "Crime Drama"),
    ("Raatchasan (2018)", "Crime Thriller"),
    ("Jigarthanda (2014)", "Crime Drama"),

    # South Indian / Pan India
    ("Baahubali (2015)", "Action Fantasy"),
    ("Baahubali 2 (2017)", "Action Fantasy"),
    ("KGF (2018)", "Action Crime"),
    ("KGF 2 (2022)", "Action Crime"),
    ("Pushpa (2021)", "Action Crime"),
    ("Pushpa 2 (2024)", "Action Crime"),
]

# Create DataFrame
df = pd.DataFrame(movies, columns=["title", "genres"])

# Add ID
df.insert(0, "movieId", range(1, len(df) + 1))

# Save
df.to_csv("D:/movie_recommendation_system/data/movie.csv", index=False)

print("Expanded dataset created successfully!")
print("Total movies:", len(df))