# aggiungi_prodotti.py - aggiunge prodotti a _data/catalogo.json + pagina _negozio/prodotto-<id>.md (IT) con tr.en nei dati.
# Uso: python automation/aggiungi_prodotti.py   (lancia dalla radice della repo; salta gli id gia' presenti; JSON ensure_ascii=False)
# Per nuovi lotti: cambia solo la lista P. Campi: id, categoria, nome, prezzo (centesimi), breve, materiale, per_chi, icona, en_nome, en_breve
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cp = os.path.join(R, "_data", "catalogo.json")
d = json.load(open(cp, encoding="utf-8"))
esistenti = {p["id"] for p in d["prodotti"]}
cats = {c["id"] for c in d["categorie"]}

P = [
 ("rosario-paracord-tasca", "rosari-e-corone", "Rosario Paracord da Tasca a Una Decade", 790,
  "Rosario a una decade in cordino paracord nero con crocifisso e medaglia, piccolo e resistente.",
  "Cordino paracord, crocifisso e medaglia in metallo.", "Per chi vuole il rosario sempre con se, in tasca o nello zaino.", "\U0001F4FF",
  "Paracord Pocket Rosary, One Decade", "One-decade rosary in black paracord cord with crucifix and medal, small and hard-wearing."),
 ("bracciale-decenario-ulivo", "rosari-e-corone", "Bracciale Decenario in Legno d'Ulivo", 690,
  "Bracciale a una decade con grani in legno d'ulivo su filo elastico e piccola croce.",
  "Grani in legno d'ulivo, filo elastico, croce in legno.", "Per chi prega con un rosario discreto da portare al polso; ottimo regalo.", "\U0001F4FF",
  "Olive Wood Decade Bracelet", "One-decade bracelet with olive wood beads on elastic cord and a small cross."),
 ("statua-addolorata-resina", "statue-e-crocifissi", "Statua Madonna Addolorata in Resina 30 cm", 3990,
  "Statua della Madonna Addolorata in resina dipinta, circa 30 cm, per la Settimana Santa e la casa.",
  "Resina dipinta a mano, altezza circa 30 cm.", "Per devoti della Settimana Santa, parrocchie e confraternite.", "\u26EA",
  "Our Lady of Sorrows Resin Statue 30 cm", "Hand-painted resin statue of Our Lady of Sorrows, about 30 cm, for Holy Week and the home."),
 ("statua-cristo-caduto-resina", "statue-e-crocifissi", "Statua Cristo Caduto in Resina", 3490,
  "Statua di Gesu che cade sotto la croce, in resina dipinta, soggetto tipico delle processioni di Settimana Santa.",
  "Resina dipinta a mano; misure da confermare col fornitore.", "Per chi cerca un soggetto per la Settimana Santa, per casa o chiesa.", "\u26EA",
  "Fallen Christ Resin Statue", "Statue of Jesus falling under the cross, in painted resin, a classic Holy Week procession subject."),
 ("set-mini-statue-santi-12cm", "statue-e-crocifissi", "Set 3 Mini Statue Santi 12 cm", 1990,
  "Tre piccole statue in resina: San Francesco, Sant'Antonio e Santa Rita, da mensola o scrivania.",
  "Resina dipinta, altezza circa 12 cm ciascuna.", "Per chi vuole piu santi in poco spazio, o come regalo.", "\u26EA",
  "Set of 3 Mini Saint Statues 12 cm", "Three small resin statues: Saint Francis, Saint Anthony and Saint Rita, for a shelf or desk."),
 ("statua-bambino-gesu-praga", "statue-e-crocifissi", "Statua Bambino Gesu di Praga in Resina 20 cm", 2790,
  "Statua del Bambino Gesu di Praga con corona e veste rossa e oro, in resina dipinta.",
  "Resina dipinta a mano, altezza circa 20 cm.", "Per devoti del Bambino Gesu di Praga e come regalo.", "\u26EA",
  "Infant Jesus of Prague Resin Statue 20 cm", "Infant Jesus of Prague statue with crown and red and gold robe, in painted resin."),
 ("magneti-ricordino-comunione-set-10", "prima-comunione", "Set 10 Magneti Ricordino Prima Comunione", 1490,
  "Dieci magneti in legno con calice e ostia, ricordino economico da consegnare agli invitati.",
  "Legno con magnete, confezione da 10 pezzi.", "Per famiglie che organizzano la Comunione e cercano ricordini a basso costo.", "\U0001F54A",
  "Set of 10 First Communion Keepsake Magnets", "Ten wooden magnets with chalice and host, a low-cost keepsake to give to guests."),
 ("pergamena-ultima-cena-comunione-set-10", "prima-comunione", "Set 10 Pergamene Ultima Cena per Comunione", 1290,
  "Dieci piccole pergamene ricordo con l'Ultima Cena, legate con nastro, da consegnare agli invitati.",
  "Carta effetto pergamena con nastro, confezione da 10.", "Per ricordini economici di Prima Comunione.", "\U0001F54A",
  "Set of 10 Last Supper Communion Scrolls", "Ten small keepsake scrolls showing the Last Supper, tied with ribbon, to give to guests."),
 ("croci-legno-cordino-set-10", "prima-comunione", "Set 10 Croci in Legno con Cordino", 1290,
  "Dieci piccole croci in legno con cordino, ricordino per Comunione, Cresima e Battesimo.",
  "Legno con cordino, confezione da 10 pezzi.", "Per ricordini da distribuire agli invitati a un sacramento.", "\u271D\uFE0F",
  "Set of 10 Wooden Crosses with Cord", "Ten small wooden crosses on cord, a keepsake for Communion, Confirmation and Baptism."),
 ("quadretto-angelo-custode-culla", "battesimo", "Quadretto Angelo Custode per Culla", 1790,
  "Piccolo quadretto con l'angelo custode che protegge un bambino, da appendere sopra la culla.",
  "Stampa su supporto rigido con cornice leggera; misure da confermare.", "Per regalo di nascita e Battesimo.", "\U0001F47C",
  "Guardian Angel Picture for a Crib", "Small picture of a guardian angel watching over a child, to hang above the crib."),
 ("corona-avvento-legno", "presepi-e-natale", "Corona d'Avvento in Legno con 4 Candele", 2490,
  "Corona d'Avvento in legno con quattro candele e decori verdi, per le quattro domeniche prima di Natale.",
  "Legno e decori; candele incluse.", "Per famiglie, scuole e parrocchie.", "\U0001F384",
  "Wooden Advent Wreath with 4 Candles", "Wooden Advent wreath with four candles and green decoration, for the four Sundays before Christmas."),
 ("mini-presepe-tavolo-legno", "presepi-e-natale", "Mini Presepe da Tavolo in Legno", 1490,
  "Piccolo presepe in legno con capanna e Sacra Famiglia, da tavolo o mensola.",
  "Legno e resina; misure da confermare.", "Per chi ha poco spazio o cerca un regalo di Natale.", "\U0001F384",
  "Small Wooden Tabletop Nativity", "Small wooden nativity with stable and Holy Family, for a table or shelf."),
 ("bue-asinello-presepe-set", "statuine-e-accessori-presepe", "Bue e Asinello per Presepe in Resina", 1290,
  "Coppia di statuine bue e asinello in resina dipinta per completare la Natività.",
  "Resina dipinta; scala da scegliere in base al presepe.", "Per chi completa o rinnova il presepe.", "\U0001F384",
  "Ox and Donkey Resin Figures for Nativity", "Pair of painted resin ox and donkey figures to complete the Nativity."),
 ("stella-cometa-led-presepe", "statuine-e-accessori-presepe", "Stella Cometa con Luce LED per Presepe", 990,
  "Stella cometa con coda dorata e luce LED calda, da mettere sopra la capanna.",
  "Plastica e LED; alimentazione da verificare col fornitore.", "Per presepi domestici di ogni misura.", "\u2B50",
  "Comet Star with LED Light for Nativity", "Comet star with golden tail and warm LED light, to place above the stable."),
 ("lumini-defunti-vetro-set-12", "candele-e-incenso", "Set 12 Lumini in Vetro Rosso per Defunti", 1290,
  "Dodici portalumini in vetro rosso con lumino, per ricordare i defunti al cimitero o a casa.",
  "Vetro rosso e lumini; adatti anche per l'esterno al riparo dal vento.", "Per il 2 novembre, le tombe di famiglia e le candele di suffragio.", "\U0001F56F\uFE0F",
  "Set of 12 Red Glass Candles for the Departed", "Twelve red glass candle holders with tea lights, to remember the departed at the cemetery or at home."),
 ("croce-capezzale-sacro-cuore", "regali-ricorrenze", "Croce da Capezzale con Sacro Cuore", 1990,
  "Croce da capezzale in legno con piccola immagine del Sacro Cuore, da appendere sopra il letto.",
  "Legno con immagine stampata; misure da confermare.", "Per chi vuole un segno di fede in camera da letto; regalo per Battesimo o matrimonio.", "\u271D\uFE0F",
  "Bedside Cross with Sacred Heart", "Wooden bedside cross with a small Sacred Heart image, to hang above the bed."),
]

n = 0
for (i, c, nome, pr, breve, mat, perchi, ic, en_nome, en_breve) in P:
    if i in esistenti or c not in cats:
        print("salto", i); continue
    d["prodotti"].append({
        "tipo": "fisico", "id": i, "nome": nome, "categoria": c, "prezzo_centesimi": pr,
        "descrizione": breve,
        "descrizione_completa": "Materiale e lavorazione\n" + mat + "\nPer chi e pensato\n" + perchi,
        "immagine": "assets/images/prodotti/" + i + ".webp", "icona": ic, "visibile": True,
        "tr": {"en": {"nome": en_nome, "descrizione": en_breve}}})
    pag = os.path.join(R, "_negozio", "prodotto-" + i + ".md")
    open(pag, "w", encoding="utf-8", newline="\n").write(
        '---\nlayout: negozio-prodotto\ntitle: "%s"\npid: %s\npermalink: /negozio/%s/\ndescription: "%s"\nref: shop-prod-%s\n---\n'
        % (nome.replace('"', "'"), i, i, breve.replace('"', "'"), i))
    n += 1
open(cp, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=2))  # MAI ensure_ascii=True
json.load(open(cp, encoding="utf-8"))  # rilettura di controllo
print("aggiunti", n, "totale", len(d["prodotti"]))
