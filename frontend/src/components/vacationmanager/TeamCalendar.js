import React from "react";
import UserCalendar from "./MonthlyCalendar";
import { getDateInfo, getNextWeekDay, getDayFromIndex } from "../../helper";
import { getMaxDaysinMonth } from "../../helper";

const TeamCalendar = () => {
    const dateInfo = getDateInfo()
    const teamMembers = ["Rahulsagar Voduru", "Fabian Mareyen", "Christoph Juergensdfffffffffffff", "Max Pitschi"]
    var rows = []
    var weekdaysMap = {}
    var count = 0
    const startDay = dateInfo.dayofmonth  
    const startMonthIndex = dateInfo.month // Date object gives month index from 0 to 11 
    const startYear = dateInfo.year
    var runningWeekdayIndex = (dateInfo.weekdayindex) - 1 // Date object gives weekday index from 1 to 7
    const maxDays = getMaxDaysinMonth(startYear, startMonthIndex)
    for(var i = startDay; count <= 30; i++){
        if(i === startDay){
            rows.push(i)
            weekdaysMap[i] = [runningWeekdayIndex, getDayFromIndex(runningWeekdayIndex).slice(0, 2)]
        }else{
                if(i <= maxDays){
                    rows.push(i)
                    const [nextIndex, nextWeekDay] = getNextWeekDay(runningWeekdayIndex)
                    runningWeekdayIndex = nextIndex
                    weekdaysMap[i] = [nextIndex, nextWeekDay]
                }else{
                    i = 0
                }
            }
        count++
    }
    return (
        <div className="TeamCalendarContainer">
            <div className="UserCalendarContainer">
                <div className="UserName UserNameDummy">Team Calendar</div>
                <div className="MonthlyCalendarContainer">
                    {
                       rows.map(weekday => {
                            var clsName = "CalendarDay CalendarDayHeader" 
                            if(weekday === 31){
                                clsName = clsName + " " + "CalendarMonthEnd"  
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