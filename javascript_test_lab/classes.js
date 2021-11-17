class Materializer {
    constructor(target) {
        this.target = target;
    }
    activated = false;
    activate() {
        this.activated = true;
    }
    materialize() {
        if (this.activated)
            return this.target;

    }
}