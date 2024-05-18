from random import choice

landmark = "CN Tower"

bird = "Red-winged Blackbird"

flower = "Trillium grandiflorum"

sport = "The Toronto Raptors"


def randomfunfact():

     funfact = [
     "Toronto is one of the most multicultural cities in the world, with over half of its residents born outside of Canada.",
     "Toronto is a major center for the film industry, hosting the Toronto International Film Festival (TIFF), one of the largest and most prestigious film festivals in the world.",
     "Toronto has an extensive underground pedestrian network known as the PATH, which spans over 30 kilometers (18.6 miles) and connects various downtown buildings, shopping centers, and transportation hubs.",
     "Toronto's Museum & Arts Pass (MAP) provides free admission for library cardholders to some of the city's top cultural institutions, including the Royal Ontario Museum (ROM) and the Art Gallery of Ontario (AGO)."
    ]

     index = choice("0123")

     print(funfact[int(index)])


if __name__ == "__main__":
    randomfunfact()

## check module.py
