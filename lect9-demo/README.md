# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)


# Self-serve instructions
If you want to do this demo yourself without seeing me do it in advance, feel free to follow these instructions:

Today, we'll be using basic React state to create a one-player Tic Tac Toe app! As always, these instructions will start very specific and slowly increase the amount of content you have to fill in.


## 1. Setup
Run
```
npx create-react-app lect14-activity
```
And replace the contents of `App.js` and `App.css` with the files in [this folder](https://github.com/cs540-s25/setup-and-demos/tree/master/lect9-demo).

If you're using Replit, fork [this directory](https://replit.com/@replit/Create-React-App) and update `App.js` and `App.css` to match the files in the repo. You'll need to add `import React from 'react';` to `App.js` at the top to get it to build.

## 2. Looking around
`App.js` defines three components: `Game`, `Board`, and `Square`. Take a minute and try to answer the following questions:
- Run `npm start` and look at the app. Can you point out instances of the three components?
- Where in the code does the "Next player: X" label come from?
- What kind of information do you think the div with class `game-info` should hold?
- **Challenge:** Why would we split out a `renderSquare()` method instead of just directly saying `<Square\>` on lines 21-23, etc?

## 3. Refresher: props
Let's temporarily set up our `Square` component so that the number of the square is written in it. To do that, we'll have to do three things:
1. Add a `props` argument to the `Square` function definition: `function Square(props) {`
2. Add an attribute to the `<Square/>` returned in `renderSquare()`: `return <Square value={i}\>`. Note that we need curly braces here because we're accessing a variable.
3. Display that attribute by adding `{props.value}` inside the `<button>` tag of `Square`.

If you reload the page now, you should see numbers written inside every square of the board.

## 4. Your first hook
Now, let's make each `Square` contain an `X` when it's been clicked. At the top of your `App.js` file, import the `useState` hook:

```
import React, {useState} from 'react';
```

And set up a piece of state for the `Square()` component before the `return` statement in that function:
```
const [value, setValue] = useState(null)
```
Here, `null` is the initial value of `value`.

Finally, we'll need to display that value inside the square. Replace `{props.value}` with `{value}` in the `<button>` tag's contents:
```
<button className="square">
  {value}
</button>
```

## 5. Handling clicks
Now, we need to make each square responsive to clicks. We'll do this by setting the `onClick` attribute of the `<button>` returned by each `Square`.

`onClick` expects a function with no arguments, so let's set the state of `value` to `"X"`:
```
<button className="square" onClick={() => setValue("X")}>
```

Now, when you load your page, you should be able to click an "X" into each square!

However, this board isn't much fun to interact with -- you can only click it 9 times. Now try to expand your `onClick()` function so that if the current value of `value` is `null`, it will be set to `"X"`, but if it's already `"X"`, it's set back to `null`. 

## 6. Putting state in the right place
*(At this point, the instructions will get slightly less specific about how to write each line of code)*

Right now, each square maintains its own state. This is a workable design, but how can we figure out who's winning the Tic Tac Toe game? With the code structured as is, we can't. We could make it so that we could pull the values out of all the squares and evaluate those when needed, but that code would be hard to read and maintain (bonus question: why?).

Instead, we can make our code easier to understand by passing state down from parent components to their children. **This is a common design pattern in React, and strongly encouraged in all situations.** Remember, React will re-render parts of the page when they change, so if the board's state is changed, any squares relying on that state will re-render. That's what makes this design pattern work!

So, the goal of this section is to maintain the list of square values in the `Board` component instead, and **pass those values down** to the appropriate squares. Start by adding a new piece of state to the `Board` component with an array of nine values. Here's a good initial value:

```
Array(9).fill(null)
```
In addition, you should clean up your `value` hook from the `Square` component -- you won't need it anymore.

Now, `renderSquare(i)` should return a `Square` with the `i`th square's value attached as the `value` attribute:

```
return <Square value={squares[i]}/>
```

Assuming you named your state variable `squares`.

Finally, we need to handle clicks in a different way. **This is a tricky concept**, so try to sit with it until it makes sense, or ask for help. Since we're passing state down from `Board` into `Square`, the `Square` itself doesn't have enough information when it's clicked to know what to do. We need to define an `onClick` function for the button in our square, but once we're inside `Square()`, we don't have access to the variable containing the different square values anymore!

Instead, we need to define a `handleClick()` function for `Board()` **and pass that down as a prop to each Square**. That way, we can write `handleClick` so that it changes the state of our board, **even though it's ultimately called from Square**. Then, the changed state value in `Board` will cause clicked squares to re-render with their new values.

```
handleClick(i) {
  const squares = squares.slice();
  squares[i] = 'X';
  setSquares(squares);
}
```
Then, you need to send down an `onClick` **prop** to each `Square` in `renderSquare()`, and the value of that prop should be `handleClick(i)` (If you were wondering before, that's why we have this `renderClick()` function defined separately!)

## 7. Making the game work

Tic Tac Toe doesn't make much sense when only X's can be played. Now we'll need to give `Board` another piece of state: what letter we're going to display on a clicked square. To do that, you'll need to:
- Add another `useState()` hook to `Board` representing the current letter being played.
- Update the letter being played inside `handleClick()`
- Stop squares that are already filled in from being updated on click (this should also happen inside `handleClick()` -- check if `squares[i]` is null!)
- Update the "Next player: X" label to use the board's state instead of a hard-coded value.

## 8. Compute a winner
It would be nice if the game would tell us when someone has won, just in case the user doesn't know how Tic Tac Toe works! 
1. Write a function that takes the board's `squares` state and figures out if someone has won the game.
2. Add a piece of state to either the `Board` or the `Game` that tracks whether there has been a winner. If someone has won the game, display a message above or below the board, and don't allow further moves!

## 9. Stretch goals
If you're a React expert, or want to really push yourself, try some of the following features:
- Change the styling so that Xs and Os show up in different colors, or are replaced by completely different images.
- Add a "new game" button that resets the board.
- Add a computer-controlled opponent for the user to play against. Assign a random side to the user every time a new game is started.
- Change up the game to one of its chaotic variations: examples include a 4x4 board, ultimate Tic Tac Toe (where each square is claimed by winning a Tic Tac Toe game contained in that square -- players can select one of the sub-game squares at a time), or any of the variants described [here](https://en.wikipedia.org/wiki/Tic-tac-toe_variants).
- Anything else you can think of!

