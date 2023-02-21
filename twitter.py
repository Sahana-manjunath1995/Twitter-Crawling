import requests
import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "root",
        db='twitter_data',
        )

cur = conn.cursor()

def get_userid(twitter_handle_csv_file):

    with open( twitter_handle_csv_file, 'r') as csvfile:
        user_ids = []
        for row in csvfile:
            striped_row = row.strip()
            url = f'https://api.twitter.com/2/users/by?usernames={striped_row}'
            headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAP4qaAEAAAAAQLdKy1LJZtknLd%2BM%2BC7VcXjhxF4%3DvIE2eFTZhBXVziuc6C42i8ekfWLEToA4Ng1OMIhqxXKeCxHSL4'}
            resp = requests.get(url, headers=headers)
            result = resp.json()
            users = result["data"]
            for user  in users:
                user_ids.append(user["id"])

    return user_ids


def get_posts(user_id, next_token=None):

    if next_token:
        url = f'https://api.twitter.com/2/users/{user_id}/tweets?pagination_token={next_token}&max_results=100'

    else:
        url = f'https://api.twitter.com/2/users/{user_id}/tweets?max_results=100'

    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAP4qaAEAAAAAQLdKy1LJZtknLd%2BM%2BC7VcXjhxF4%3DvIE2eFTZhBXVziuc6C42i8ekfWLEToA4Ng1OMIhqxXKeCxHSL4'}
    resp = requests.get(url, headers=headers)
    result = resp.json()
    value = result["data"]
    next_token = result['meta'].get( 'next_token', None)
    posts = []
    for i in value:
        details = [user_id, i['id'], i["text"]]
        posts.append(details)

    return posts, next_token


if __name__ == '__main__':
    twitter_handle_csv_file = 'twitter_handle.csv'
    user_id_list = get_userid( twitter_handle_csv_file)
    print(user_id_list)
    for user_id in user_id_list:
        next_token = None
        data_list = []
        while True:
            posts, next_token = get_posts(user_id, next_token)
            data_list = data_list + posts
            if not next_token:
                break

    for row in data_list:
        mysql_query ='''
        Insert into user_postdetails (user_id, post_id, post_text) values (%s, %s, %s)
        '''
        result = cur.execute(mysql_query, row)
    conn.commit()












