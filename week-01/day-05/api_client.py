import requests
class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    def get_all_posts(self)->list:
        url = f"{self.BASE_URL}/posts"
        response = self.make_request(url)        
        return response.json()
    def get_user_detail(self, user_id:int)->dict:
        url = f"{self.BASE_URL}/users/{user_id}"
        response = self.make_request(url)                
        return response.json()
    def get_post_by_id(self, post_id: int)->dict:
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.make_request(url)        
        return response.json()
    def make_request(self, endpoint: str):
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        return response

def main():
    client = ApiClient()

    try:
        # Task 1: Get all posts
        posts = client.get_all_posts()

        print("Status: Success")
        print("Total Posts:", len(posts))
        print("First Post Title:", posts[0]["title"])

        # Task 2: Get user details
        user = client.get_user_detail(2)

        print("\nUser Details")
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])

        try:
            post = client.get_post_by_id(9999)
        except requests.exceptions.HTTPError as error:
            print("Post not found:", error.response.status_code)
        else:
            print("\nPost Details")
            print(post)
    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except (KeyError, IndexError) as error:
        print("Unexpected API response:", error)


if __name__ == "__main__":
    main()