import { Button } from '@mui/material';
import React from 'react';
import getMonthFromIndex from '../../helper'
import { getDateInfo, getMaxDaysinMonth } from '../../helper';

const CalendarNav = ({ currentStartDay, currentMonthIndex, currentYear, updateFunc }) => {
    const monthId = getMonthFromIndex(currentMonthIndex).slice(0, 3)
    const monthIndexStr = String(currentMonthIndex)
    const thisYear = getDateInfo().year
    const thisYearStr = String(thisYear)
    const prevYearStr = String(thisYear - 1)
    const nextYearStr = String(thisYear + 1)
    
    const monthOnChange = (event) => {
        const value = parseInt(event.target.value)
        const year = document.getElementById("Year").value
        updateFunc(year, value, 1)
    }
    
    const yearOnChange = (event) => {
        const value = parseInt(event.target.value)
        const monthIndex = document.getElementById("Month").value
        updateFunc(value, monthIndex, 1)
    }

    const calendarMoveRight = (event) => {
        var nextStartDay = currentStartDay
        var nextMonthIndex = currentMonthIndex + 1
        var nextYear = currentYear
        if(currentMonthIndex === 11){
            // If right clicked when Dec is shown it should go to Jan of next year
            nextMonthIndex = 0
            nextYear = nextYear + 1     
        } 
        const maxDaysinMonth = getMaxDaysinMonth(nextYear, nextMonthIndex)
        if(nextStartDay > maxDaysinMonth){
            nextMonthIndex++
            nextStartDay = nextStartDay - maxDaysinMonth
        }
        updateFunc(nextYear, nextMonthIndex, nextStartDay)
    }

    const calendarMoveLeft = (event) => {
        var nextStartDay = currentStartDay
        var prevMonthIndex = currentMonthIndex - 1
        var prevYear = currentYear
        if(currentMonthIndex === 0){
            // If left clicked when Jan is shown it should go to Dec of prev year
            prevMonthIndex = 11
            prevYear = currentYear - 1     
        } 
        const maxDaysinMonth = getMaxDaysinMonth(prevYear, prevMonthIndex)
        if(nextStartDay > maxDaysinMonth){
            nextStartDay = maxDaysinMonth
        }
        updateFunc(prevYear, prevMonthIndex, nextStartDay)
    }
    return (
        <div className='CalendarNav'>
            <div>
                <select id="Month" onChange={monthOnChange}>
                    {currentMonthIndex === 0 ? <option value="0" selected>Jan</option> : <option value="0">Jan</option>}
                    {currentMonthIndex === 1 ? <option value="1" selected>Feb</option> : <option value="1">Feb</option>}
                    {currentMonthIndex === 2 ? <option value="2" selected>Mar</option> : <option value="2">Mar</option>}
                    {currentMonthIndex === 3 ? <option value="3" selected>Apr</option> : <option value="3">Apr</option>}
                    {currentMonthIndex === 4 ? <option value="4" selected>May</option> : <option value="4">May</option>}
                    {currentMonthIndex === 5 ? <option value="5" selected>Jun</option> : <option value="5">Jun</option>}
                    {currentMonthIndex === 6 ? <option value="6" selected>Jul</option> : <option value="6">Jul</option>}
                    {currentMonthIndex === 7 ? <option value="7" selected>Aug</option> : <option value="7">Aug</option>}
                    {currentMonthIndex === 8 ? <option value="8" selected>Sep</option> : <option value="8">Sep</option>}
                    {currentMonthIndex === 9 ? <option value="9" selected>Oct</option> : <option value="9">Oct</option>}
                    {currentMonthIndex === 10 ? <option value="10" selected>Nov</option> : <option value="10">Nov</option>}
                    {currentMonthIndex === 11 ? <option value="11" selected>Dec</option> : <option value="11">Dec</option>}
                </select>

                <select id="Year" onChange={yearOnChange}>
                    {currentYear === thisYear - 1 ? <option value={prevYearStr} selected>{prevYearStr}</option> : <option value={prevYearStr}>{prevYearStr}</option>}
                    {currentYear === thisYear ? <option value={thisYearStr} selected>{thisYearStr}</option> : <option value={thisYearStr}>{thisYearStr}</option>}                    
                    {currentYear === thisYear + 1 ? <option value={nextYearStr} selected>{nextYearStr}</option> : <option value={nextYearStr}>{nextYearStr}</option>}
                    
                </select>
            </div>
            <div>
                <button className='CalendarNavBtn' onClick={calendarMoveLeft}>{'<'}</button>
                <button className='CalendarNavBtn' onClick={calendarMoveRight}>{'>'}</button>
            </div>
        </div>
    )
}

export default CalendarNav