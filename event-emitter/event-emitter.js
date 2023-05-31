class EventEmitter {
    constructor() {
        this.events = {};
    }

    subscribe(event, cb) {
        // If no handlers for current event - initialize an empty list
        this.events[event] = this.events[event] ?? [];
        this.events[event].push(cb);

        return {
            unsubscribe: () => this.events[event].pop(),
        };
        //To avoid memory leaks adding a cleanup condition
        if (this.events[event].length=== 0) { delete this.events[event] }
    }

    emit(event, args = []) {
        if (!(event in this.events)) return [];
        return this.events[event].map(f => f(...args));
    }
}