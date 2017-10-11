import fresh_tomatoes
import media
""" Establish objects containing movie details """

two_towers = media.Movie("The Lord of the Rings: The Two Towers",
                         "While Frodo and Sam edge closer to Mordor with the \
                         help of the shifty Gollum, the divided fellowship \
                         makes a stand against Sauron's new ally, Saruman, \
                         and his hordes of Isengard.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=cvCktPUwkW0")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                                  "The adventure continues in this 'Star \
                                  Wars' sequel. Luke Skywalker (Mark Hamill), \
                                  Han Solo (Harrison Ford), Princess Leia \
                                  (Carrie Fisher) and Chewbacca (Peter \
                                  Mayhew) face attack by the Imperial forces \
                                  and its AT-AT walkers on the ice planet \
                                  Hoth. While Han and Leia escape in the \
                                  Millennium Falcon, Luke travels to Dagobah \
                                  in search of Yoda. Only with the Jedi \
                                  master's help will Luke survive when the \
                                  dark side of the Force beckons him into the \
                                  ultimate duel with Darth Vader (David \
                                  Prowse).",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=xESiohGGP7g")  # NOQA

holy_grail = media.Movie("Monty Python and the Holy Grail",
                         "A comedic send-up of the grim circumstances of the \
                         Middle Ages as told through the story of King Arthur \
                         and framed by a modern-day murder investigation. \
                         When the mythical king of the Britons leads his \
                         knights on a quest for the Holy Grail, they face a \
                         wide array of horrors, including a persistent Black \
                         Knight, a three-headed giant, a cadre of \
                         shrubbery-challenged knights, the perilous Castle \
                         Anthrax, a killer rabbit, a house of virgins, and a \
                         handful of rude Frenchmen.",
                         "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",  # NOQA
                         "https://www.youtube.com/watch?v=scD4_ZVDD-8")

dark_knight = media.Movie("The Dark Knight",
                          "When the menace known as the Joker emerges from \
                          his mysterious past, he wreaks havoc and chaos on \
                          the people of Gotham, the Dark Knight must accept \
                          one of the greatest psychological and physical \
                          tests of his ability to fight injustice.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=kmJLuwP3MbY")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "Two imprisoned men bond over a number of \
                                   years, finding solace and eventual \
                                   redemption through acts of common decency.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")  # NOQA

twelve_angry_men = media.Movie("12 Angry Men",
                               "A jury holdout attempts to prevent a \
                               miscarriage of justice by forcing his \
                               colleagues to reconsider the evidence.",
                               "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=8JhjvSE1JpA")

movies = [two_towers, empire_strikes_back, holy_grail, dark_knight,
          shawshank_redemption, twelve_angry_men]

fresh_tomatoes.open_movies_page(movies)
