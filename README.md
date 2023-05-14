# A Simple TODO App for ChatGPT Plugin

A proof-of-concept ToDo ChatGPT Plugin using Python.

The primary value of this repository is to replicate the experience of developing the ChatGPT plugin for the first time. You will quickly gain experience developing ChatGPT plugin.

# Instructions
Here is my memo. You can also follow this instruction.

1. Watch the instruction video.

ChatGPT plugins developer experience:
https://openai.com/blog/chatgpt-plugins

As you may notice, the video content is getting older.

2. Generate a simple TODO app code using ChatGPT.

Open ChatGPT and change GPT-4 mode. Then execute the following prompt. This prompt is from the instruction video. (Thanks for the provided instruction video from OpenAI!)

Used Prompt:
```
Write a simple TODO app using FastAPI, that lets the user add TODOs, list their TODOs, and delete TODOs.

Include a `__main__` section which will run this app using uvicorn. The Python module where I save this code will be called `main.py`.

In addition to the normal endpoints, include a route `/.well-known/ai-plugin.json` which serves (as JSON) the contents of `./manifest.json`, located in the same directory as `main.py`. Exclude this route from the OpenAPI spec, and don’t serve any other static content.
```

You will get differnt code and will not work properly. Retry generating the code, and if that does not work, modify it manually.

Add the following code to service `openapi.yaml`.

```python
# Added manually after code generation.
@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    return FileResponse('openapi.yaml')
```

3. Sing up [CodeSandbox](https://codesandbox.io/) for developing and deploying our app.

4. Create a python environment on CodeSandbox.

5. Add dependency libraries to `requirements.txt`

6. Restart the environment to create the updated container for us.

7. Copy the content of the generated code and paste it into the `main.py`.

8. Create a `manifest.json` on the top directory.

Here is `manifest.json`. Replace `<YOUR_SERVER>` in `https://<YOUR_SERVER>/openapi.yaml` with your environment.

```json
{
    "schema_version": "v1",
    "name_for_human": "TODO Demo",
    "name_for_model": "todo_demo",
    "description_for_human": "TODO demo app",
    "description_for_model": "An app for managing a user's TODOs",
    "auth": {
        "type": "none"
    },
    "api": {
        "type": "openapi",
        "url": "https://<YOUR_SERVER>/openapi.yaml",
        "is_user_authenticated": false
    },
    "logo_url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Yes_Check_Circle.svg",
    "contact_email": "support@example.com",
    "legal_info_url": "http://www.example.com/legal"
}
```

9. Restart again to deploy the app.

10. Access the `https://<SERVER NAME>/openapi.json` to get OpenAPI specification.

I got the specification like this:
```
{"openapi":"3.0.2","info":{"title":"Simple TODO API","description":"This is a very simple TODO API","version":"1.0.0"},"paths":{"/todos":{"get":{"summary":"Get Todos",
[...]
```

11. Copy the OpenAPI specification and paste it into [Swagger Editor](https://editor.swagger.io/) to convert json to yaml. Create `openapi.yaml` on the top directory and paste the yaml.

12. Almost done. All you need to do is to register the plugin with ChatGPT. Open ChatGPT and then open `Plugin store` and then click `Develop your own plugin`. After that, follow the instruction shown in the display.

13. Voilà! ChatGPT now uses our TODO apps.

Here is a screen capture.

