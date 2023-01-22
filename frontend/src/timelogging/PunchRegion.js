import React, { useState, useEffect } from 'react';
import axios from 'axios';

const punch_url = 'http://127.0.0.1:8000/punch/';

const PunchRegion = (props) => {
    const [liveState, setliveState] = useState(props['livestate']);
    function recordPunchin(){
      const punch_in_entry = {
          log_user: props['login_name'],
          log_date: "2023-01-22",
          log_in_time: "18:00:00",
          log_state: 0
        }
      axios.post(punch_url, punch_in_entry, {
        headers: {
          Accept: 'application/json'
        }
      }).then().catch(err => console.log(err));
    }
    function recordPunchout(){
      const punch_out_entry = {
          log_user: props['login_name'],
          log_date: "2023-01-22",
          log_out_time: "19:30:00",
          log_state: 0
        }
      axios.post(punch_url, punch_out_entry, {
        headers: {
          Accept: 'application/json'
        }
      }).then().catch(err => console.log(err))
    }
    const punchinButtonEnable = liveState === 0 ? true : false;
    const punchoutButtonEnable = liveState === 0 ? false : true; 
    return (
        <div>
               <button disabled={punchinButtonEnable} onClick={recordPunchin}>Punch-In</button>
               <button disabled={punchoutButtonEnable} onClick={recordPunchout}>Punch-Out</button>
        </div>
    );
}

export default PunchRegion