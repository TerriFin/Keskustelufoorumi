# Keskustelufoorumi

Tässä projektissa teen yksinkertaisen foorumin johon käyttäjät pystyvät luoda ja jatkaa viestiketjuja.
Lopullisessa versiossa ainoastaan käyttäjät jotka ovat tehneet postauksen/kommentin pystyvät muokata/poistaa kyseisen julkaisun, ja lopullisessa versiossa tulee myös olemaan jonkinsorttinen "hall of fame", josta löytyvät ne käyttäjät jotka ovat tehneet parhaat postaukset.

Joitakin valmiita käyttäjiä joita löytyy foorumilta;

username: test 
password: test

username: hello
password: world

**[Tietokannoista](https://github.com/TerriFin/Keskustelufoorumi/blob/master/documentation/Tietokannoista.md)**

**[Käyttötapauksia](https://github.com/TerriFin/Keskustelufoorumi/blob/master/documentation/kayttotapaukset.md)**

**Linkki herokuun: https://bestforumever.herokuapp.com**

Tällä hetkellä hall of fame ei toimi herokussa, koska postgres vaatii erilaista kyselyä kuin sqlite3. Minun pitää keksiä tapa millä herokussa
applikaatio käyttää seuraavaa kyselyä tämänhetkisen kyselyn sijasta:

SELECT Post."postName", Post."accountId", COUNT(Comment.id) FROM Post LEFT JOIN Comment ON Post.id = comment."postId" GROUP BY Post."postName", Post."accountId" ORDER BY Count(Comment.id) DESC LIMIT 1;

Tuskin kerkiän tehdä sitä ennen seuraavaa deadlineä, joten laitan tmän nyt tähän armon toivossa.
