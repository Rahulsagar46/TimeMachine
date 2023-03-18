import React from "react";
import {useState} from 'react';
import UserCalendar from "./UserCalendar";
import MonthHeader from "./MonthHeader";
import CalendarNav from "./CalendarNav";
import { getDateInfo, getNextWeekDay, getDayFromIndex } from "../../helper";
import { getMaxDaysinMonth } from "../../helper";

const TeamCalendar = () => {
    const [dateInfo, setdateInfo] = useState(getDateInfo())
    const [teamMembers, setTeamMembers] = useState(["XXXX1", "YYYYY1", "ZZZZ1", "MMMMM1"])
    
    const dateObjUpdate = (year, monthIndex, day) => {
        const newDateObj = new Date(year, monthIndex, day)
        const newDateInfo = getDateInfo(newDateObj)
        setdateInfo(newDateInfo)
    }

    const groupMembersUpdate = (event) => {
        const value = event.target.value
        var members = []
        if(value === "default"){
            members = ["XXXX1", "YYYYY1", "ZZZZ1", "MMMMM1"]
        } else if (value === "G2"){
            members = ["XXXX1", "YYYYY1", "MMMMM1"]
        } else{
            members = ["XXXX1", "YYYYY1"]
        }
        setTeamMembers(members)
    }
    const startDay = dateInfo.dayofmonth 
    const startMonthIndex = dateInfo.month // Date object gives month index from 0 to 11 
    const startYear = dateInfo.year
    const maxDaysonCalendar = 30

    var rows = []
    var weekdaysMap = {}
    var count = 0
    var runningWeekdayIndex = (dateInfo.weekdayindex) // Date object gives weekday index from 0:Sunday to 7:Saturday
    var runningMonthIndex = startMonthIndex
    
    var monthYearDateMap = {}
    monthYearDateMap[runningMonthIndex] = {"year" : startYear, "start" : startDay}
    
    var monthIndexList = [runningMonthIndex]
    var maxDays = getMaxDaysinMonth(startYear, runningMonthIndex)
    var nextYear = startYear
    var key = ""
    var monthChange = false
    for(var i = startDay; count <= maxDaysonCalendar; i++){ 
        key = String(i) + "-" + String(runningMonthIndex) + "-" + String(nextYear)
        if(i <= maxDays){
            rows.push(key)
            if(i === startDay && monthChange === false){
                weekdaysMap[key] = [runningWeekdayIndex, getDayFromIndex(runningWeekdayIndex).slice(0, 2)]
            }else{
                const [nextIndex, nextWeekDay] = getNextWeekDay(runningWeekdayIndex)
                runningWeekdayIndex = nextIndex
                weekdaysMap[key] = [nextIndex, nextWeekDay]
            }
            if(i === maxDays){
                monthYearDateMap[runningMonthIndex]["end"] = i
            }
        }else{
            // If the second month in the view is from another year
            i = 0
            if(runningMonthIndex === 11){
                runningMonthIndex = 0
                nextYear++
            }else{
                runningMonthIndex++
            } 
            monthIndexList.push(runningMonthIndex)
            maxDays = getMaxDaysinMonth(nextYear, runningMonthIndex)
            monthYearDateMap[runningMonthIndex] = {"year" : nextYear, "start" : 1}
            monthChange = true
        }
    
        if(count === maxDaysonCalendar){
            monthYearDateMap[runningMonthIndex]["end"] = i
        }
        count++
    }
    return (
        <div className="TeamCalendarContainer">
            <div className="UserCalendarContainer MonthHeaderContainer">
                <div className="CalendarNavContainer">
                    <CalendarNav currentStartDay={startDay} currentMonthIndex={startMonthIndex} currentYear={startYear} updateFunc={dateObjUpdate}/>
                </div>
                <div className="MonthlyCalendarContainer">
                    {
                        monthIndexList.map(monthIndex => {
                            return (
                                <MonthHeader monthIndex={monthIndex} 
                                            year={monthYearDateMap[monthIndex]["year"]}  
                                            startDate={monthYearDateMap[monthIndex]["start"]} 
                                            endDate={monthYearDateMap[monthIndex]["end"]}
                                            maxDaysonCalendar={maxDaysonCalendar}
                                />
                            )
                        })
                    }
                </div>
            </div>
            <div className="UserCalendarContainer">
                <div className="UserName UserNameDummy">
                    <div style={{fontWeight: "bold"}}>Team Calendar</div>
                    <div className="GroupSelector">
                        <select id="Group" onChange={groupMembersUpdate}>
                            <option value="default" selected>All</option>
                            <option value="G1">Group-1</option>
                            <option value="G2">Group-2</option>
                        </select>
                    </div> 
                </div>
                <div className="MonthlyCalendarContainer">
                    {
                       rows.map(weekday => {
                            var clsName = "CalendarDay CalendarDayHeader" 
                            if(parseInt(weekday.split("-")[0]) === 1){
                                clsName = clsName + " " + "CalendarMonthStart"  
                            }
                            return (
                                <div className={clsName}>{weekdaysMap[weekday][1]}</div>
                            )
                        })
                    }
                </div>
            </div>    
            { teamMembers.map(member => {
                return (
                        <UserCalendar user={member} displayDates={rows} weekdaysMap={weekdaysMap}/>
                        )
                    }
                )
            }
        </div>       
    )
} 
export default TeamCalendar