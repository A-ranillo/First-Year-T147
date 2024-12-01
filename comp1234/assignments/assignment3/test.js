describe('Part 2: Comparing Numbers', function() {
    it('should return 2 when num1 > num2', function() {
        chai.expect(part2(5, 3)).to.equal(2);
    });

    it('should return 1 when num1 < num2', function() {
        chai.expect(part2(2, 4)).to.equal(1);
    });

    it('should return 0 when num1 == num2', function() {
        chai.expect(part2(3, 3)).to.equal(0);
    });
});

describe('Part Three: Loop and Concatenation', function() {
    it('should generate ascending sequence when  num1 < num2', function() {
        chai.expect(part3(1, 20)).to.equal('1234567891011121314151617181920');
    });

    it('should generate descending sequence when num1 > num2', function() {
        chai.expect(part3(14, 4)).to.equal('1413121110987654');
    });

    it('should sum the numbers when num1 == num2', function() {
        chai.expect(part3(3, 3)).to.equal(6);
    });
});

describe('Part Four: Array Index Check', function() {
    it('should return true for a valid index within array bounds', function() {
        chai.expect(part4(1, [10, 20, 30])).to.be.true;
    });

    it('should return false for an index equal to array length', function() {
        chai.expect(part4(3, [10, 20, 30])).to.be.false;
    });

    it('should return false for a negative index', function() {
        chai.expect(part4(-1, [10, 20, 30])).to.be.false;
    });

    it('should return false for an index in an empty array', function() {
        chai.expect(part4(0, [])).to.be.false;
    });
});

describe('Part Five: Array Summation', function() {
    it('should concatenate even numbers', function() {
        chai.expect(part5([1, 2, 3, 4])).to.equal('24');
    });

    it('should return 0 if there are no even numbers', function() {
        chai.expect(part5([1, 3, 5])).to.equal(0);
    });

    it('should return 0 for an empty array', function() {
        chai.expect(part5([])).to.equal(0);
    });

    it('should handle an array with only even numbers', function() {
        chai.expect(part5([2, 4, 6])).to.equal('246');
    });

    it('should handle an array with zeros', function() {
        chai.expect(part5([0, 1, 2])).to.equal('02');
    });
});