def generate_recommendation(quiz_answers):
    weekend_activity = quiz_answers.get('weekend_activity', '')
    gender_age = quiz_answers.get('gender_age', '')

    recommendation = ''

    if weekend_activity == 'formal':
        if gender_age == 'male':
            recommendation = 'オフィスでおすすめのメガネは、スクエア型です。'
        elif gender_age == 'female':
            recommendation = 'オフィスでおすすめのメガネは、ボストン型です。'
    elif weekend_activity == 'creative':
        if gender_age == 'male':
            recommendation = 'カフェやラウンジでおすすめのメガネは、ウェリントン型です。'
        elif gender_age == 'female':
            recommendation = 'カフェやラウンジでおすすめのメガネは、ウェリントン型です。'
    elif weekend_activity == 'casual':
        if gender_age == 'male':
            recommendation = '自宅でのくつろぎの時間にはラウンド型のメガネがおすすめです。'
        elif gender_age == 'female':
            recommendation = '自宅でリラックスするなら、ラウンド型のメガネがおすすめです。'
    elif weekend_activity == 'sports':
        if gender_age == 'male':
            recommendation = 'スポーツを楽しむなら、アウトドア用のスポーティなメガネが必要です。'
        elif gender_age == 'female':
            recommendation = 'スポーツ時にはスポーティなメガネがおすすめです。'
    elif weekend_activity == 'outdoor':
        if gender_age == 'male':
            recommendation = 'アウトドアでの活動にはラウンド型のメガネが適しています。'
        elif gender_age == 'female':
            recommendation = 'アウトドアでのアクティビティにはラウンド型のメガネがおしゃれです。'
    else:
        recommendation = '利用シーンに合ったメガネの型を選びましょう。'

    return recommendation