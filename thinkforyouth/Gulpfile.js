'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var util = require('gulp-util');
var autoprefixer = require('gulp-autoprefixer');
var run = require('gulp-run');


gulp.task('styles', function () {
    log('Compiling SASS --> CSS');

    return gulp.src('./resources/sass/app.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({browsers: ['last 2 version', '> 5%']}))
        .pipe(gulp.dest('./utils/static/css'));
});

gulp.task('collect', ['styles'], function () {
    log('Collecting static files...');
    run('python manage.py collectstatic --noinput').exec();
});

gulp.task('sass:watch', function() {
    log('Watching SCSS files for change...');
    gulp.watch(['./resources/sass/*.scss'], ['collect']);
});

function log(msg) {
    if (typeof(msg) === 'object') {
        for (var item in msg) {
            if (msg.hasOwnProperty(item)) {
                util.log(util.colors.blue(msg[item]));
            }
        }
    } else {
        util.log(util.colors.blue(msg));
    }
}
