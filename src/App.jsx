
import './App.css';
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import {Inject, ScheduleComponent, Day, Week, WorkWeek, Month, Agenda} from '@syncfusion/ej2-react-schedule';

class App extends React.Component{
render() {
  return <ScheduleComponent height='550px' selectedDate= {new Date(2018, 1, 15)} eventSettings={ { dataSource: this.data } } >
    <Inject services={[Day, Week, WorkWeek, Month, Agenda]}/>
  </ScheduleComponent>
}
};
ReactDOM.render(<App />, document.getElementById('schedule'));

export default App;