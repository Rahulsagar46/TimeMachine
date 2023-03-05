import React from 'react';
import SubSection from './SubSection';
import LeftSubcomponent from './LeftSubcomponent';

const TimeLoggingContainer = ({initialinfo, setInitialinfo }) => {
    return (
        <div className='TimeLoggingMainContainer'>
            <LeftSubcomponent initialinfo={initialinfo} setInitialinfo={setInitialinfo}/>
            <SubSection initialinfo={initialinfo} setInitialinfo={setInitialinfo}/>
        </div>
    );
}

export default TimeLoggingContainer