import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const myTitle = "Todo List"
  const [todos, setTodos] = useState(["finish this demo"]);
  const [inputVal, setInputVal] = useState("");

  function handleClick() {
    const newTodos = [...todos, inputVal];
    setTodos(newTodos);
  }

  function handleChange(event) {
    setInputVal(event.target.value);
  }

  return (
    <div className="App">
      <h1>{myTitle}</h1>
      <input placeholder="Add a todo" value={inputVal} onChange={handleChange} />
      <button onClick={handleClick()}>Submit</button>
      <ul>
        {todos.map((todo) => <li>{todo}</li>)}
      </ul>
    </div>
  );
}

export default App;
