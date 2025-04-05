from flask import Flask, jsonify, request
import requests
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

GITHUB_API_URL = "https://api.github.com/users/"

@app.route('/github/<username>', methods=['GET'])
def get_github_profile(username):
    logging.info(f"Fetching profile for {username}")
    
    response = requests.get(f'{GITHUB_API_URL}{username}')
    
    if response.status_code == 200:
        data = response.json()
        profile_image = data['avatar_url']
        public_repos = data['public_repos']

        return jsonify({
            'username': username,
            'profile_image': profile_image,
            'public_repos': public_repos
        })
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
