# Minicade

My goal is to use pyxel to create a beautiful tic tac toe game and use the knowledge I gain from this to create more complex games in the future using the same engine.

# Model View Controller Architecture

## Model:

Provides core internal and external functionality for interacting with the state of the entire application.

## View:

The controller tells the view what to render.

## Controller

The controller is in charge of getting data from the model, processing actions taken by the user, and updating the view as needed.

With this architecture, we should be able to swap out any piece as long as it still uses the basic functionalities provided by the other two pieces. For example, we should be able to easily switch betwen command line terminal output and a compex UI for playing a sophisticated game of tic tac toe.
