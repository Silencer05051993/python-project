from chalice import Chalice, Response, CORSConfig

app = Chalice(app_name='playads-deliver')
app.debug = True

cors_config = CORSConfig(allow_origin='*',
                         allow_headers=['Origin', 'X-Requested-With', 'Content-Type', 'Accept', 'Token'],
                         allow_credentials=True)


@app.route('/helloworld', methods=['GET'], cors=cors_config)
def helloworld():
    status_code = 200
    headers = {'Content-Type': 'application/json'}
    body = {'message': 'Welcome dimage share'}
    return Response(status_code=status_code, headers=headers,
                    body=body)
