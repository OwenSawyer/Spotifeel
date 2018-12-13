from music import SpotifyService

if __name__=='__main__':
    # Just for testing..
    with open('C:/Users/Owen/Desktop/spotify.txt', 'r') as fp:
        env = fp.readlines()
        env = [i.strip() for i in env]

    # token = util.prompt_for_user_token(env[1], env[0], client_id=env[2],
    #                                    client_secret=env[3],
    #                                    redirect_uri='http://localhost:8888/callback')
    # print(token)
    sp = SpotifyService(input('Enter token: '))

    print(sp.get_audio_analysis('5Q4mP2MPgZelC7soOeeARX'))
