
class HolbertonCourse {
    constructor(name, length, students) {
        this._name = '';
        this._length = 0;
        this._students = [];

        this.name = name; // Calls the setter for validation
        this.length = length; // Calls the setter for validation
        this.students = students; // Calls the setter for validation
    }

    get name() {
        return this._name;
    }

    set name(newName) {
        if (typeof newName !== 'string')
        this._name = newName;
    }

    get length() {
        return this._length;
    }

    set length(newLength) {
        this._length = newLength;
    }

    get students() {
        return this._students;
    }

    set students(newStudents) {
        this._students = newStudents;
}

export default HolbertonCourse;
