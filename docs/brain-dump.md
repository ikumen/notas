## 💡 **This page is just brain dump of raw ideas, feel free to add to it** 💡

## What

* markdown based note-taking web app
* support tags
* support search of title, content, tags
* minimal editing experience (check out dev.to for example)
* edit/preview modes (maybe side by side)
* signin with OAuth (e.g openid connect)
* categories?
* (future) export/archive to github gist, dropbox, download?
* (future) think about OT (operational transformations) for colab editing

#### Tech
* Python backend (leaning toward [Starlette](https://www.starlette.io/) or Flask)
* TypeScript (and JS) frontend (leaning toward [Svelte](https://svelte.dev), maybe Vue, React)
* Azure (App Service, Functions, CosmosDB)
* Redis for an inverted index implementation for simple search


## How

**I'm putting these out there to give us some direction, something concrete to discuss, I'm open to suggestions** 

### Frontend  app architecture

Just a Svelte SPA that loads CodeMirror instance for editing. Kinda hacked together as I'm learning svelte. I'm up for starting refactoring/starting over if some one more knowledgeable.

```shell
frontend/
   app/
      components/           
         codemirror.css        # styling for codemirror
         Content.svelte        # content view component, renders markdown 
         ContentEditor.svelte  # component that loads codemirror for editing
         Editor.svelte         
         LastUpdated.svelte    
         Mode.svelte           # component for toggling between edit/split/preview
         note.css              
         NoteList.svelte       # list of notes component
         PageLayout.svelte
         PrivacyToggle.svlete  
         Tags.svelte           # tags view component
         TagsEditor.svelte     # tags editing component
         Title.svelte          # title view component
         TitleEditor.svelte    # title editing component
         Viewer.svelte         # displays Title, Tags and Content
      pages/                   # Page/views within our SPA
      services/
          NoteService.ts       # handles request to backend /api/notes
      App.svelte               # main app entry point
      helpers.ts               # utils
      index.ts                 # loads the app entry point
      note.ts                  # type def for a Note
   public/
   package.json
   rollup.config.js            # like webpack, build and bundles svelte components
   tsconfig.json               # config for TypeScript use
```

### Backend app architecture

Just an idea to get us started, lets iterate and evolve/refine it.

```shell
backend/
   app/
      templates/
      datastore.py     # encapsulate calls to underlying datastore, can get fancy and make it interface with concrete impl for different databases (crazy talk, this is not Java)
      routes.py        # route def and mappings, might need to break out. need one set for spa and api
      service.py       # manages interactions between route handler to underlying datastore or some other business logic
      settings.py      # self expl, let's model after 12-factor, all config from environment vars
   main.py
```


### Data model for notes

Maybe start with just using dictionary? at a minimum we should capture:

**Note**
 - id (use mongo id or self generate???)
 - user ?? maybe just a str for now until we hook in Auth/user
 - title: str (required??)
 - content: str = None
 - ispublic: bool = False (private by default)
 - tags: List[str]
 - category: str (just a path e.g, /courses/udacity/cloud-developer)  


### Initial API

/api/notes         GET return list of all notes
/api/notes/<id>    GET reutrn a note by id
/api/notes         POST create a note
/api/notes/<id>    PUT update a note
/api/notes/<id>    DELETE delete a note
/api/notes/search  GET search for notes (terms in query string)

### Authentication

For much later, use OAuth, Github at a minimum
- for who ever is gonna work on it, take a [look at authlib](https://docs.authlib.org/en/stable/)
- I've implemented 


## Why

* looking for a new job soon, want to have a new project showcasing skills for tech I'm interested in working in
* start simple, maybe move on to more complicated projects together