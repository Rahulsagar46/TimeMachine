import React , { useEffect, useState } from 'react';
import './App.css';
import Header from './components/global/Header';
import CheekletBar from './components/global/CheekletBar';
import ContentContainer from './components/global/ContentContainer';
import axios from 'axios';

const user = "rahulv"
const url = 'http://127.0.0.1:8000/' + user;

function App() {
  console.log("APP loading")
  const [initialinfo, setInitialinfo] = useState({});
  function getInitialInfo(){
    console.log("fetch initial info")
    axios(url, {
      headers: {
        Accept: 'application/json'
      }
    }).then(res => setInitialinfo(res.data)).catch(err => console.log(err));
  }
  
  useEffect(() => {
    getInitialInfo();
  }, []);
  
  return (
    <div className="App">
      <Header initialinfo={initialinfo}/>
      <CheekletBar />
      <ContentContainer initialinfo={initialinfo} setInitialinfo={getInitialInfo}/>
    </div>
  );
}

export default App;
