import json

from com.dimageshare.algorithm.kmean_algorithm import KmeanAlgorithm


class UserService(object):

    def make_result(self):
        data = KmeanAlgorithm().read_data()
        df = KmeanAlgorithm().kmean_clustering(data)

        json_data = []
        json_el0 = {}
        json_el0['label'] = 0

        json_el1 = {}
        json_el1['label'] = 1
        json_el2 = {}
        json_el2['label'] = 2
        json_el3 = {}
        json_el3['label'] = 3
        json_el4 = {}
        json_el4['label'] = 4

        cluster0 = []
        cluster1 = []
        cluster2 = []
        cluster3 = []
        cluster4 = []

        for index, row in df.iterrows():
            user_id = row['user_id']
            gender = row['gender']
            age = row['age']
            salary = row['salary']
            spending_score = row['spending_score']
            label = int(row['label'])

            json_child = {}
            json_child['user_id'] = user_id
            json_child['gender'] = gender
            json_child['age'] = age
            json_child['salary'] = salary
            json_child['spending_score'] = spending_score

            if label == 0:
                cluster0.append(json_child)
            elif label == 1:
                cluster1.append(json_child)
            elif label == 2:
                cluster2.append(json_child)
            elif label == 3:
                cluster3.append(json_child)
            else:
                cluster4.append(json_child)

        json_el0['users'] = cluster0
        json_el1['users'] = cluster1
        json_el2['users'] = cluster2
        json_el3['users'] = cluster3
        json_el4['users'] = cluster4

        json_data.append(json_el0)
        json_data.append(json_el1)
        json_data.append(json_el2)
        json_data.append(json_el3)
        json_data.append(json_el4)


        return json.dumps(json_data)

if __name__ == '__main__':
    UserService().make_result()
