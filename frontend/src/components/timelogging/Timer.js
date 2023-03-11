import React from "react";
import { useState, useEffect } from "react";
import {getDateInfo} from "../../helper"
import {getHoursFromSeconds, getElapsedTimeSinceTarget, getRemainingTime} from "../../helper"

const Timer = ( {initial_info} ) => {
    const getTimeStart = (initial_info) =>{
        const mandatory_work_time  = initial_info["mandatory_working_time_per_day"]
        const mandatory_break_time = initial_info["mandatory_break_time"]
        const todaysDateInfo = getDateInfo()
        if(initial_info["log_entries"].length === 0){
            return (getRemainingTime(mandatory_work_time, mandatory_break_time, 0))
        }
        for (let i=0; i < initial_info["log_entries"].length; i++){
            if(initial_info["log_entries"][i]["date"] === todaysDateInfo.dateformat2){
                const todayLogCount = initial_info["log_entries"][i]["log_entries"].length
                if(todayLogCount === 0){
                    return (getRemainingTime(mandatory_work_time, mandatory_break_time, 0))    
                }
                let elapsedTime = 0
                for (let j=0; j < todayLogCount; j++){
                    if (initial_info["log_entries"][i]["log_entries"][j]["log_state"] === 0){
                        elapsedTime = elapsedTime + getElapsedTimeSinceTarget(initial_info["log_entries"][i]["log_entries"][j]["log_in_time"])
                    }
                    else{
                        elapsedTime = elapsedTime + initial_info["log_entries"][i]["log_entries"][j]["interval_time"]
                    }
                }
                return (getRemainingTime(mandatory_work_time, mandatory_break_time, elapsedTime))            
            }
        }
        return (getRemainingTime(mandatory_work_time, mandatory_break_time, 0))
    }
    const startVal = initial_info["log_entries"] !== undefined ? getTimeStart(initial_info) : null 
    const [elapsedHours, setElapsedHours] = useState(getHoursFromSeconds(startVal))
    
    // timer effect happens here
    useEffect(() => {
        if((initial_info["live_state"] === 0) || startVal===0){
            return
        }
        const timeout = setTimeout(() => {
            setElapsedHours(getHoursFromSeconds(startVal - 1));
        }, 1000);
    
        return () => {
          clearTimeout(timeout);
        };
      }, [elapsedHours, initial_info["live_state"]]);
    
      return (
            <div className='TimerContainer'>
                <div className="TimerContainerSubComponent">
                    <div className="TimerHeader">Mandatory Work Time</div>
                    <div className="ElapsedTime">{getHoursFromSeconds(initial_info["mandatory_working_time_per_day"])}</div>
                </div>
                <div className="TimerContainerSubComponent">
                    <div className="TimerHeader">Mandatory Break Time</div>
                    <div className="ElapsedTime">{getHoursFromSeconds(initial_info["mandatory_break_time"])}</div>
                </div>
                <div className="TimerContainerSubComponent">
                    <div className="TimerHeader">Remaining Work Time</div>
                    <div className="ElapsedTime">{elapsedHours}</div>
                </div>
            </div>
        ) 
}

export default Timer