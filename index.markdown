---
layout: index
title: Damon Snyder
...

    % if properties.has_key('posts'):
        <ul class="posts">
            % for post in properties['posts']:
                <li><span>${post.date}</span> &raquo; <a href="${post.url}">${post.title}</a></li>
            % endfor
        </ul>
    % else:
        <h2>Error, no posts available!</h2>
    % endif
