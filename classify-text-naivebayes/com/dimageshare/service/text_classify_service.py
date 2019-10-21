import pandas as pd

from com.dimageshare.algorithm.naivebayes_algorithm import NaiveBayesAlgorithm
import json


class TextClassificationService(object):
    def __init__(self):
        self.test = None

    def train_data(self):
        train_data = []
        train_data.append({"feature": "Datamining là gì?", "target": "datamining_bigdata"})
        train_data.append({"feature": "Bigdata có gì vui không", "target": "datamining_bigdata"})
        train_data.append({"feature": "Các thuật toán hay dùng cho lĩnh vực đó", "target": "datamining_bigdata"})
        train_data.append({"feature": "Các thuật toán đó có ứng dụng gì cho cty chúng ta được không",
                           "target": "datamining_bigdata"})
        train_data.append({"feature": "Nên dùng giải thuật nào cho bài toán này", "target": "datamining_bigdata"})
        train_data.append({"feature": "Món gì ngon ở Hà Nội", "target": "cuisine"})
        train_data.append({"feature": "Bún chả obama ở đường nào", "target": "cuisine"})
        train_data.append({"feature": "Hoa quả dầm Tô Tịch mùi vị thế nào", "target": "cuisine"})
        train_data.append(
            {"feature": "Gà mạch hoạch ngon quá", "target": "cuisine"})
        train_data.append(
            {"feature": "Kem hồ Tây và kem Tràng Tiền, loại nào ngon hơn", "target": "cuisine"})
        train_data.append(
            {"feature": "Ở đây người ta không bán thịt chó", "target": "cuisine"})
        df_train = pd.DataFrame(train_data)

        return df_train

    def make_result(self, str):
        test_data = []
        test_data.append({'feature': u'' + str})
        df_test = pd.DataFrame(test_data)
        naive_bayes_model = NaiveBayesAlgorithm()
        df_train = self.train_data()
        init = naive_bayes_model.init.fit(df_train["feature"], df_train.target)
        predicted = init.predict(df_test["feature"])
        predict_proba = init.predict_proba(df_test["feature"])

        data = {}

        data['predicted'] = predicted[0]
        data['datamining_bigdata_estimator'] = predict_proba[0][1]
        data['cuisine_estimator'] = predict_proba[0][0]

        json_obj = json.dumps(data)
        return json_obj


if __name__ == '__main__':
    tcp = TextClassificationService()
    tcp.make_result('Bún chả làm thế nào')
