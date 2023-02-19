import React, { useState, useEffect } from 'react';
import axios from 'axios';

const punch_url = 'http://127.0.0.1:8000/punch/';

const PunchRegion = ({login_name, livestate, setInfo}) => {
    const is_user_in = livestate === 0 ? false : true

    function getDateAndTime(){
        const dateObj = new Date()
        const todaysDate = dateObj.getFullYear()+'-'+(dateObj.getMonth() + 1)+'-'+dateObj.getDate()
        const currentTime = dateObj.getHours()+':'+dateObj.getMinutes()+':'+dateObj.getSeconds()

        return [todaysDate, currentTime]
    }

    function recordPunchin(){
      const [todaysDate, currentTime] = getDateAndTime()
      const punch_in_entry = {
          log_user: login_name,
          log_date: todaysDate,
          log_in_time: currentTime,
          log_state: 0
        }
      axios.post(punch_url, punch_in_entry, {
        headers: {
          Accept: 'application/json'
        }
      }).then(() => {
        setInfo(prevState => {
          return { ...prevState, live_state: 1}
        })}).catch(err => console.log(err));
    }
    
    function recordPunchout(){
      const [todaysDate, currentTime] = getDateAndTime()
      const punch_out_entry = {
          log_user: login_name,
          log_date: todaysDate,
          log_out_time: currentTime,
          log_state: 0
        }
      axios.post(punch_url, punch_out_entry, {
        headers: {
          Accept: 'application/json'
        }
      }).then(() => {
        setInfo(prevState => {
          return { ...prevState, live_state: 0}
        })}).catch(err => console.log(err))
    }
    return (
        <div>
               <button disabled={is_user_in} onClick={recordPunchin}>Punch-In</button>
               <button disabled={!is_user_in} onClick={recordPunchout}>Punch-Out</button>
        </div>
    );
}

export default PunchRegion