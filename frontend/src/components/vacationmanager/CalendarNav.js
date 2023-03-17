import { Button } from '@mui/material';
import React from 'react';
import getMonthFromIndex from '../../helper'

const CalendarNav = ({ currentMonthIndex, currentYear, updateFunc}) => {
    const monthId = getMonthFromIndex(currentMonthIndex).slice(0, 3)
    const monthNum = String(currentMonthIndex + 1)
    const thisYear = String(currentYear)
    const prevYear = String(currentYear - 1)
    const nextYear = String(currentYear + 1)
    
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
    return (
        <div className='CalendarNav'>
            <div>
                <select id="Month" onChange={monthOnChange}>
                    <option value="0">Jan</option>
                    <option value="1">Feb</option>
                    <option value="2">Mar</option>
                    <option value="3">Apr</option>
                    <option value="4">May</option>
                    <option value="5">Jun</option>
                    <option value="6">Jul</option>
                    <option value="7">Aug</option>
                    <option value="8">Sep</option>
                    <option value="9">Oct</option>
                    <option value="10">Nov</option>
                    <option value="11">Dec</option>
                    <option value={monthNum} selected>{monthId}</option>
                </select>

                <select id="Year" onChange={yearOnChange}>
                    <option value={prevYear}>{prevYear}</option>
                    <option value={currentYear} selected>{currentYear}</option>
                    <option value={nextYear}>{nextYear}</option>
                </select>
            </div>
            <div>
                <button className='CalendarNavBtn'>{'<'}</button>
                <button className='CalendarNavBtn'>{'>'}</button>
            </div>
        </div>
    )
}

export default CalendarNav