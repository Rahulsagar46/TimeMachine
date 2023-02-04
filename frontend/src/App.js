import React , { useEffect, useState } from 'react';
import './App.css';
import Header from './Header';
import PunchRegion from './timelogging/PunchRegion';
import CheekletBar from './CheekletBar';
import axios from 'axios';

const url = 'http://127.0.0.1:8000/rvoduru';

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
      <PunchRegion login_name={initialinfo['login_name']} livestate={initialinfo['live_state']} setInfo={setInitialinfo}/>
    </div>
  );
}

export default App;
