import pusher

pusher_client = pusher.Pusher(
    app_id='1518560',
    key='1fb64f027f5f40e81a79',
    secret='1785068556fa75087922',
    cluster='us2',
    ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})