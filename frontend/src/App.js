

import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleQuerySubmit = async () => {
    try {
      const res = await axios.get('http://localhost:8000/query', {
        params: { text: query },
      });
      setResponse(res.data.response);
    } catch (error) {
      console.error('Error making request:', error);
      setResponse('Error occurred while fetching data');
    }
  };

  return (
    <div className="App">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your query"
      />
      <button onClick={handleQuerySubmit}>Submit Query</button>
      <div>{response}</div>
    </div>
  );
}

export default App;
