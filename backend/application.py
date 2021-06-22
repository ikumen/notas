from backend.app import factory


app = factory.create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('backend.application:app', host='0.0.0.0', port=5000, reload=True, log_level='info')
