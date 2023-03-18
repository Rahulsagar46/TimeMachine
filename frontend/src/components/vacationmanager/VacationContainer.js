import React from "react";
import LeftNavBar from "./LeftNavBar";
import TeamCalendar from "./TeamCalendar";
import VacationForm from "./VacationForm";
import AbsenceStatusOverview from './AbsenceStatusOverview'

const VacationContainer = () => {
    return (
        <div className="VacationContainer">
            <div className="VacationSubSection1">
                <TeamCalendar />
                <VacationForm />
            </div>
            <div className="VacationSubSection2">
                <AbsenceStatusOverview /> 
            </div>
        </div>
    )
}

export default VacationContainer