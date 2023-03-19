import React from "react";
import {useState, useEffect} from 'react';
import axios from 'axios';
import TeamCalendar from "./TeamCalendar";
import VacationForm from "./VacationForm";
import AbsenceStatusOverview from './AbsenceStatusOverview'

const user = "rahulv"
const url = 'http://127.0.0.1:8000/teamcalendar/' + user;

const VacationContainer = () => {
    const [teamCalendarInfo, setTeamCalendarInfo] = useState({});
    function getInitialInfo(){
        axios(url, {
        headers: {
                Accept: 'application/json'
            }
        }).then(res => setTeamCalendarInfo(res.data)).catch(err => console.log(err));
    }
    useEffect(() => {
        getInitialInfo();
    }, []);
    
    const splitComponents = () => {
        if(! ("common" in teamCalendarInfo)){
            return [null, null, null]
        }
        const holidays = teamCalendarInfo["holidays"]
        const planned  = teamCalendarInfo["planned"]
        const applied  = teamCalendarInfo["applied"]
        const holidayList = []
        const plannedMap = {}
        const appliedMap = {}
        var holidayFormatted = ""
        for(let i=0; i < holidays.length; i++){
            holidayFormatted = holidays[i]["day"] + "-" + holidays[i]["month"] + "-" + holidays[i]["year"]
            holidayList.push(holidayFormatted)
        }
        for(let i=0; i < planned.length; i++){
            var entry = planned[i]
            if(!(entry["user"] in plannedMap)){
                plannedMap[entry["user"]] = []
            }
            holidayFormatted = entry["day"] + "-" + entry["month"] + "-" + entry["year"]
            plannedMap[entry["user"]].push(holidayFormatted)
        }
        for(let i=0; i < applied.length; i++){
            var entry = applied[i]
            if(!(entry["user"] in appliedMap)){
                appliedMap[entry["user"]] = []
            }
            holidayFormatted = entry["day"] + "-" + entry["month"] + "-" + entry["year"]
            appliedMap[entry["user"]].push(holidayFormatted)
        }
        return [holidayList, plannedMap, appliedMap]
    }

    const [holidayList, plannedMap, appliedMap] = splitComponents()
    
    return (
        ("common" in teamCalendarInfo) ?
        <div className="VacationContainer">
            <div className="VacationSubSection1">
                <TeamCalendar holidayList={holidayList} plannedMap={plannedMap}/>
                <VacationForm />
            </div>
            <div className="VacationSubSection2">
                <AbsenceStatusOverview plannedList={plannedMap[user]} appliedList={appliedMap[user]}/> 
            </div>
        </div> : null
    )
}

export default VacationContainer