from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/"

@app.route('/github/<username>', methods=['GET'])
def get_github_profile(username):
    response = requests.get(f"{GITHUB_API_URL}{username}")
    
    if response.status_code == 200:
        data = response.json()
        profile_image = data.get('avatar_url')
        repo_count = data.get('public_repos')

        return jsonify({
            'username': username,
            'profile_image': profile_image,
            'repository_count': repo_count
        })
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
