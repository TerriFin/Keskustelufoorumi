![image](https://user-images.githubusercontent.com/32302869/43494969-2b925138-953e-11e8-9e5b-6385898ae86f.png)

Yllä oleva kuva kuvaa tietokantataulujen suhteita toisiinsa.


Käyttäjällä, jolta tallennetaan id, käyttäjätunnus ja salasana on monia postauksia ja kommentteja.

Postauksilla ja kommenteilla sensijaan on aina vain yksi käyttäjä joka on tehnyt ne, ja kommentit liittyvät aina yhteen postaukseen, mutta postauksella voi olla useita kommentteja.


Postauksista tallennetaan niiden id, postauksen nimi (joka näytetään etusivulla), postauksen postaus aika, muokkaus aika ja postauksen luoneen käyttäjän id.

Kommenteista tallennetaan id, kommentin sisältö, postaus aika, muokkaus aika, sen postauksen id mihin kommentti on tehty ja kommentin tehneen käyttäjän id.
