module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            sass: {
                files: '*.scss',
                tasks: ['sass']
            }
        },
        sass: {
            dev: {
                files: {
                    'css/main.css': 'sass/main.scss'
                }
            }
        },
        browserSync: {
            default_options: {
                bsFiles: {
                    src: ['*.css', '*.html']
                },
                options: {
                    watchTask: true,
                    server: {
                        baseDir: "./",
                        directory: true,
                        index: "index.html"
                    }
                }
            }
        }
    });

    // load npm tasks
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');

    // define default task
    grunt.registerTask('default', ['browserSync', 'watch']);
};