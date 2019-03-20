import tabula as tb
import pandas as pd
import json as json
import io as io


class Naslov:
    def __init__(self, zaporedna_st, postna_stevilka, naziv_poste, naselje, ulica, hisna_st, dodatek):
        self.zaporedna_st = zaporedna_st
        self.postna_stevilka = postna_stevilka
        self.naziv_poste = naziv_poste
        self.naselje = naselje
        self.ulica = ulica
        self.hisna_st = hisna_st
        self.dodatek = dodatek


def csv_convert(input_path, output_path):
    tb.convert_into(input_path, output_path, output_format="csv", pages="all")


def objects_convert(input_path):
    data = []
    df = pd.read_csv(input_path)

    for index, row in df.iterrows():
        if pd.notnull(row[0]) and pd.notnull(row[1]) and pd.notnull(row[2]) \
                and pd.notnull(row[3]) and pd.notnull(row[5]) and pd.notnull(row[7]):
            if pd.notnull(row[8]):
                n = Naslov(row[0], row[1], row[2], row[3], row[5], row[7], row[8])
            else:
                n = Naslov(row[0], row[1], row[2], row[3], row[5], row[7], "")
            data.append(n)
    return data


def json_convert(output_path, objects):
    data = json.dumps(objects, default=lambda i: i.__dict__, indent=4, ensure_ascii=False)

    with io.open(output_path, "w", encoding="utf-8") as f:
        f.write(unicode(data, "utf-8"))


if __name__ == '__main__':
    csv_convert("nabiralniki.pdf", "nabiralniki.csv")
    json_convert("nabiralniki.json", objects_convert("nabiralniki.csv"))
