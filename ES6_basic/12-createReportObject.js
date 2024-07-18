function createReportObject() {
  let allEmployees = {};

  employeesList.forEach(employee => {
    const { name, department } = employee;
    
    allEmployees = {
      ...allEmployees,
      [department]: [...(allEmployees[department] || []), name]
    };
  });

  return {
    allEmployees,
    getNumberOfDepartments() {
      return Object.keys(allEmployees).length;
    }
  };
}

export default createReportObject;
