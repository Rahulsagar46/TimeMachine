import React from 'react';
import { useState } from 'react';
import TimeLoggingSideNav from './TimeLoggingSideNav';
import SubSection from './SubSection';

const TimeLoggingContainer = ({initialinfo, setInitialinfo }) => {
    const [activeTab, setActiveTab] = useState("timeentry")
    return (
        <div className='TimeLoggingMainContainer'>
            <TimeLoggingSideNav activeTab={activeTab} setActiveTab={setActiveTab}/>
            <SubSection initialinfo={initialinfo} setInitialinfo={setInitialinfo}/>
        </div>
    );
}

export default TimeLoggingContainer