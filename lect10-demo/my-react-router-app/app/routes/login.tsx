import { useState, useEffect } from 'react';

export default function Login() {
    const [val, setVal] = useState(null)
    useEffect(() => {
        fetch("http://localhost:5000/data", {
            "method": "GET",
            "headers": {
                "Content-Type": "application/json"
            }
        }).then(response => response.json()).then(data => setVal(data.value))
    }, []); // this second [] argument is important! it means "rerun the function that was the first argument when any of these variables change"
    // since the list is empty, we will never rerun as long as the component stays rendered

    return <h1>I am a Login Page! My server-fetched value is {val}</h1>;
}